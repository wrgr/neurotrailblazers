#!/usr/bin/env ruby
# Checks checkpoint identity, source traceability and safe publication, not scientific truth.
require 'json'
require 'yaml'
require 'digest'
require 'uri'
require 'csv'

root = File.expand_path('..', __dir__)
evidence = JSON.parse(File.read(File.join(root, '_data/paper_evidence.json')))
trackers = {}
%w[core500 core500-first100].each do |scope|
  directory = File.join(root, 'docs/reviews', scope)
  tracker = JSON.parse(File.read(File.join(directory, 'tracker.json')))
  trackers[scope] = tracker
  meta, rows = tracker.fetch('metadata'), tracker.fetch('papers')
  stop = scope == 'core500' ? 500 : 100
  corpus_path = File.join(root, meta.fetch('corpus_path'))
  raise 'Corpus changed: recheck membership' unless Digest::SHA256.file(corpus_path).hexdigest == meta.fetch('corpus_sha256')
  corpus = YAML.safe_load(File.read(corpus_path), aliases: true).fetch('papers')
  expected = corpus.select { |p| p['in_top_500'] }.first(stop)
  raise 'Wrong ranks/boundary' unless rows.map { |p| p['rank'] } == (1..stop).to_a && meta['stop_after'] == stop
  raise 'Wrong membership/order' unless rows.map { |p| p['doi'] } == expected.map { |p| p['doi'].strip.downcase }
  raise 'Duplicate DOI' unless rows.map { |p| p['doi'] }.uniq.size == stop
  csv = CSV.read(File.join(directory, 'tracker.csv'), headers: true)
  raise 'CSV coverage mismatch' unless csv.size == stop
  required = %w[contribution result context limitation source_url source_locator evidence_basis checked_by checked_on uncertainty dataset_use access_notes]
  rows.zip(expected, csv).each do |row, paper, csv_row|
    raise 'Title mismatch' unless row['title'] == paper['title']
    required.each { |k| raise "Missing #{k}: #{row['rank']}" unless row[k].is_a?(String) && !row[k].strip.empty? }
    raise 'Invalid depth' unless %w[abstract_only full_text inaccessible].include?(row['review_depth'])
    %w[uncertain source_checked public_note_eligible].each { |k| raise "Invalid #{k}" unless [true, false].include?(row[k]) }
    raise 'Depth/access disagreement' unless row['source_checked'] == (row['review_depth'] != 'inaccessible')
    raise 'Status/access disagreement' unless row['status'] == (row['source_checked'] ? 'source_checked' : 'inaccessible')
    accepted = row['source_checked'] && !row['uncertain']
    raise 'Unsafe publication eligibility' unless row['public_note_eligible'] == accepted
    uri = URI.parse(row['source_url'])
    raise 'Unsafe source URL' unless uri.is_a?(URI::HTTPS) && uri.host && !uri.userinfo
    raise 'Missing local PDF checksum' unless row.fetch('local_source_pdf_sha256').match?(/\A[0-9a-f]{64}\z/)
    if !row['local_extraction_hash_matches_pdf'] && !row['local_source_issue']
      raise "Unaccounted stale extraction: #{row['rank']}"
    end
    raise 'Excerpt exceeds short verification quote' if row.fetch('source_excerpt', '').split.size > 25
    note = evidence[row['doi']]
    if accepted
      raise 'Missing public evidence' unless note
      (required - ['access_notes'] + %w[review_depth uncertain dataset_use]).each do |k|
        raise "Tracker/public drift #{row['rank']} #{k}" unless note[k] == row[k]
      end
    else
      raise 'Unresolved or inaccessible review published' if note
    end
    csv_row.headers.each do |key|
      value = row[key]
      matches = if [true, false].include?(value)
                  csv_row[key].to_s.downcase == value.to_s
                elsif key == 'local_source_issue'
                  (csv_row[key].to_s.empty? ? nil : JSON.parse(csv_row[key])) == value
                else
                  csv_row[key].to_s == value.to_s
                end
      raise "CSV/JSON disagreement #{row['rank']} #{key}" unless matches
    end
  end
  counts = {
    'reviewed' => rows.size,
    'source_checked' => rows.count { |p| p['source_checked'] },
    'abstract_only' => rows.count { |p| p['review_depth'] == 'abstract_only' },
    'full_text' => rows.count { |p| p['review_depth'] == 'full_text' },
    'uncertain' => rows.count { |p| p['uncertain'] },
    'inaccessible' => rows.count { |p| p['review_depth'] == 'inaccessible' },
    'public_note_eligible' => rows.count { |p| p['public_note_eligible'] },
    'local_source_issues' => rows.count { |p| p['local_source_issue'] }
  }
  raise 'Summary counts drifted' unless meta.fetch('counts') == counts
  puts "PASS: #{scope} exact membership, CSV/JSON agreement, source/depth/uncertainty and safe public evidence: #{counts}"
end
raise 'First100 checkpoint diverged' unless trackers['core500']['papers'].first(100) == trackers['core500-first100']['papers']
