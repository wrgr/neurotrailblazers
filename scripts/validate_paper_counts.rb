#!/usr/bin/env ruby
# frozen_string_literal: true

# Gate against documented-vs-actual drift on the journal paper hubs.
#
# The hub pages are hand-maintained markdown while the corpus they describe is a
# data file, so the two drift apart silently. They had, on three separate axes:
# a total ("100+") that no longer matched the 96 authored entries, a documented
# YAML schema listing two fields (key_figures, related_content) that exist on
# none of the 200 records, and per-dimension counts that nothing checked.
#
# This checks the claims that can be checked mechanically. It does not check
# prose.

require "yaml"
require "pathname"

ROOT = Pathname.new(__dir__).parent
INDEX = ROOT.join("content-library/journal-papers/index.md")
DATA = ROOT.join("_data/journal_papers.yml")
PAPERS_DIR = ROOT.join("content-library/journal-papers")

# A paper entry on an authored page is a numbered h2: "## 7. Author (2020) — Title".
PAPER_HEADING = /^## \d+\. /.freeze

problems = []

index_text = INDEX.read(encoding: "UTF-8")

# ---------------------------------------------------------------------------
# 1. Per-dimension counts in the index tables must match the pages they link to.
# ---------------------------------------------------------------------------
claimed = {}
index_text.each_line do |line|
  # | [Neuroanatomy]({{ '/content-library/journal-papers/neuroanatomy/' | ... }}) | 8 | ... |
  match = line.match(%r{^\|\s*\[[^\]]+\]\(\{\{\s*'/content-library/journal-papers/([a-z0-9-]+)/'.*?\)\s*\|\s*(\d+)\s*\|})
  next unless match

  claimed[match[1]] = match[2].to_i
end

if claimed.empty?
  problems << "#{INDEX.relative_path_from(ROOT)}: found no dimension rows to check — " \
              "the table format changed and this validator needs updating with it"
end

actual = {}
claimed.each_key do |slug|
  page = PAPERS_DIR.join("#{slug}.md")
  unless page.exist?
    problems << "#{INDEX.relative_path_from(ROOT)}: links to #{slug}, which does not exist"
    next
  end

  actual[slug] = page.read(encoding: "UTF-8").each_line.count { |l| l.match?(PAPER_HEADING) }
end

claimed.each do |slug, n|
  next unless actual.key?(slug)
  next if actual[slug] == n

  problems << "#{INDEX.relative_path_from(ROOT)}: claims #{n} papers for #{slug}, " \
              "but #{slug}.md contains #{actual[slug]}"
end

# ---------------------------------------------------------------------------
# 2. The stated total must match the sum of the pages.
# ---------------------------------------------------------------------------
total_actual = actual.values.sum
if (m = index_text.match(/\*\*Total:\s*(\d+)\s*papers?\*\*/))
  stated = m[1].to_i
  if stated != total_actual
    problems << "#{INDEX.relative_path_from(ROOT)}: states a total of #{stated} papers, " \
                "but the linked pages contain #{total_actual}"
  end
else
  problems << "#{INDEX.relative_path_from(ROOT)}: no '**Total: N papers**' line found to check"
end

# Any "100+"-style vague total is what drifted last time. Refuse it.
if index_text.match?(/\b\d+\+\s+(?:curated\s+)?(?:essential\s+)?papers\b/i)
  problems << "#{INDEX.relative_path_from(ROOT)}: uses an open-ended paper count " \
              "(\"N+ papers\"). State the real number; it is checked here."
end

# ---------------------------------------------------------------------------
# 3. Every field in the documented schema must exist on at least one record.
# ---------------------------------------------------------------------------
data = YAML.safe_load(DATA.read(encoding: "UTF-8"), aliases: true)
records = data.is_a?(Hash) ? data.fetch("papers", []) : Array(data)

if records.size < 200
  problems << "_data/journal_papers.yml: #{records.size} papers. A generator bug once " \
              "cut this to 1; if the drop is intentional, update this floor deliberately."
end

real_fields = records.flat_map(&:keys).uniq

if (block = index_text[/```yaml\n(.*?)```/m, 1])
  documented = block.scan(/^ {2}([a-z_]+):/).flatten.uniq
  missing = documented - real_fields
  unless missing.empty?
    problems << "#{INDEX.relative_path_from(ROOT)}: documents schema field(s) " \
                "#{missing.join(', ')} that exist on none of the #{records.size} records"
  end
end

# ---------------------------------------------------------------------------
# 4. Corpus dimension counts quoted in prose must match the data.
# ---------------------------------------------------------------------------
data_dims = records.group_by { |r| r["dimension"] }.transform_values(&:size)
index_text.scan(/`([a-z-]+)`\s*\((\d+)\)/) do |dim, n|
  next unless data_dims.key?(dim)
  next if data_dims[dim] == n.to_i

  problems << "#{INDEX.relative_path_from(ROOT)}: says #{dim} has #{n} papers in the " \
              "corpus; the data file has #{data_dims[dim]}"
end

# ---------------------------------------------------------------------------
if problems.empty?
  puts "OK: journal paper counts and schema match the data " \
       "(#{total_actual} authored across #{actual.size} dimensions, #{records.size} in corpus)"
  exit 0
end

warn "Journal paper documentation does not match the data:"
problems.each { |p| warn "  - #{p}" }
exit 1
