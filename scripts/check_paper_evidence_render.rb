#!/usr/bin/env ruby
# Actual Liquid gate and actual built output, not a reimplementation of rendering.
require 'jekyll'
require 'json'
require 'yaml'
require 'set'
root = File.expand_path('..', __dir__)
site = File.join(root, ENV.fetch('SITE_DIR','_site'))
papers = YAML.safe_load(File.read(File.join(root,'_data/journal_papers.yml')), aliases: true).fetch('papers')
records = JSON.parse(File.read(File.join(root,'_data/paper_evidence.json')))
by_id = papers.to_h { |p| [p.fetch('id'),p] }
raise 'Duplicate paper IDs' unless by_id.size == papers.size
raise 'Duplicate DOI' unless papers.map { |p| p.fetch('doi').strip.downcase }.uniq.size == papers.size
norm = ->(doi) { doi.to_s.strip.downcase }
expected_evidence = ->(p) { records[norm.call(p['doi'])] }
gate = File.read(File.join(root,'_includes/papers/evidence-gate.html'))
template = Liquid::Template.parse(gate + "{{ checked_paper_evidence.doi | default: 'none' }}")
key,record = records.first
fixtures = [[key,record,key],['10.9999/sem-unrelated',record,'none'],[key,nil,'none'],[key,record.merge('status'=>'generated'),'none'],[key,record.merge('doi'=>'10.9999/mismatch'),'none'],[key,record.merge('source_url'=>'javascript:alert(1)'),'none']]
%w[contribution result context limitation source_url source_locator evidence_basis checked_by checked_on].each { |field| fixtures << [key,record.merge(field=>'  '),'none'] }
context = Liquid::Context.new
fixtures.each do |paper_doi,candidate,want|
 context['site']={'data'=>{'paper_evidence'=>{key=>candidate}}}
 context['include']={'paper'=>{'doi'=>paper_doi}}
 got=template.render!(context).strip
 raise "Liquid gate failure for #{paper_doi}: #{got.inspect}" unless got==want
end
# Check cross-paper reset using the same context and a retained evidence table.
context['site']={'data'=>{'paper_evidence'=>records}}
[key,'10.9999/sem-unrelated',key,''].each do |d|
 context['include']={'paper'=>{'doi'=>d}}
 raise 'Evidence leaked between papers' unless template.render!(context).strip==(d==key ? key : 'none')
end
graph = JSON.parse(File.read(File.join(site,'technical-training/journal-club/graph-data.json')))
raise 'Graph lost paper records' unless graph.map{|p|p['id']}.to_set==by_id.keys.to_set && graph.size==papers.size
seen_edges=Set.new
valid_dois=papers.map{|p|norm.call(p['doi'])}.to_set
graph.each do |p|
 original=by_id.fetch(p['id'])
 %w[title authors year journal doi abstract].each { |k| raise "Metadata drift #{p['id']} #{k}" unless p[k]==original[k] }
 raise "Mismatched graph evidence #{p['id']}" unless p['evidence']==expected_evidence.call(original)
 %w[ocar summaries discussion_prompts].each { |k| raise "Generated graph field #{k}" unless p[k].nil? }
 raise 'Summary without checked evidence' if !p['evidence'] && p['summary']
 raise 'Citation drift' unless (p['cites']||[])==(original['cites']||[])
 (p['cites']||[]).each do |target|
  target=norm.call(target); source=norm.call(p['doi'])
  raise 'Dangling citation or self-edge' unless valid_dois.include?(target) && target!=source
  raise 'Duplicate citation' unless seen_edges.add?([source,target])
 end
end
[500,1000,2000].each do |tier|
 export=JSON.parse(File.read(File.join(site,"data/corpus_#{tier}.json")))
 expected=papers.select{|p|p['tier']<=tier}
 raise "Export schema #{tier}" unless export.dig('metadata','schema_version')==2
 raise "Export count #{tier}" unless export.dig('metadata','count')==expected.size && export['papers'].size==expected.size
 raise "Export membership #{tier}" unless export['papers'].map{|p|p['id']}.to_set==expected.map{|p|p['id']}.to_set
 export['papers'].each do |p|
  o=by_id.fetch(p['id'])
  %w[title authors year doi abstract].each{|k| raise "Export metadata #{p['id']} #{k}" unless p[k]==o[k]}
  raise 'Export venue drift' unless p['venue']==o['journal']
  raise 'Export evidence mismatch' unless p['evidence']==expected_evidence.call(o)
  raise 'Unverified export annotations' unless p['ocar'].nil? && p['summaries'].nil? && p['discussion_prompts']==[]
  raise 'False verified provenance' if p.key?('source_flag')
 end
end
cards={}
Dir.glob(File.join(site,'technical-training/journal-club/details/*.json')).each{|f|cards.merge!(JSON.parse(File.read(f)))}
raise 'Missing detail cards' unless cards.keys.to_set==by_id.keys.to_set
cards.each do |id,html|
 raise "Legacy annotation in #{id}" if html.match?(/jc-card-(?:ocar|expertise|streams)/) || html.include?('Reading notes and discussion (unverified)')
 has_evidence=html.include?('What this paper demonstrated')
 raise "Card evidence leak #{id}" unless has_evidence==!!expected_evidence.call(by_id[id])
end
puts "PASS actual Liquid: #{fixtures.size+4} eligibility/reset fixtures; #{papers.size} graph records and cards; #{seen_edges.size} directed citations; 3 safe public exports."
puts "Evidence coverage: #{records.size}/#{papers.size} source-checked notes; this is not a corpus-wide scientific validation."
