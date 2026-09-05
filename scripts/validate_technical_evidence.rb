#!/usr/bin/env ruby
# frozen_string_literal: true

require 'yaml'
require 'date'

ROOT = File.expand_path('..', __dir__)
track_path = File.join(ROOT, '_data', 'technical_track.yml')
evidence_path = File.join(ROOT, '_data', 'technical_evidence.yml')
capabilities_path = File.join(ROOT, '_data', 'technical_capabilities.yml')

unless File.exist?(track_path) && File.exist?(evidence_path)
  warn '[WARN] Missing technical track or technical evidence data file.'
  exit 0
end

track = YAML.safe_load(File.read(track_path, encoding: 'UTF-8'), permitted_classes: [Date], aliases: true) || {}
evidence = YAML.safe_load(File.read(evidence_path, encoding: 'UTF-8'), permitted_classes: [Date], aliases: true) || {}

track_slugs = Array(track['modules']).map { |m| m['slug'] }.compact
unit_entries = Array(evidence['units'])
unit_by_slug = unit_entries.each_with_object({}) { |u, h| h[u['slug']] = u }

paper_lib = (evidence.dig('library', 'papers') || {}).keys
dataset_lib = (evidence.dig('library', 'datasets') || {}).keys

warnings = []

track_slugs.each do |slug|
  unit = unit_by_slug[slug]
  if unit.nil?
    warnings << "[WARN] missing evidence entry for technical unit slug: #{slug}"
    next
  end

  papers = Array(unit['papers'])
  datasets = Array(unit['datasets'])
  checks = Array(unit['competency_checks'])

  warnings << "[WARN] #{slug}: fewer than 2 key papers" if papers.size < 2
  warnings << "[WARN] #{slug}: missing key dataset anchors" if datasets.empty?
  warnings << "[WARN] #{slug}: missing competency checks" if checks.empty?

  papers.each do |pid|
    warnings << "[WARN] #{slug}: unknown paper id '#{pid}'" unless paper_lib.include?(pid)
  end
  datasets.each do |did|
    warnings << "[WARN] #{slug}: unknown dataset id '#{did}'" unless dataset_lib.include?(did)
  end
end

extra = unit_by_slug.keys - track_slugs
extra.each { |slug| warnings << "[WARN] evidence entry has no matching technical unit: #{slug}" }

# ---------------------------------------------------------------------------
# Unit page <-> data reconciliation.
#
# Two mappings used to drift apart silently: the "Course links" list a learner
# reads at the foot of each unit page, and `mapped_modules` in
# technical_track.yml, which is what the rest of the site reasons about. Unit 08
# named modules 07 and 12 while the data said 06 and 07; unit 09 named 09 and 15
# against 10, 13, 14, 15, 20. The page is the thing a learner acts on, so it has
# to be checkable against the data rather than maintained by memory.

def unit_page_path(root, slug)
  File.join(root, 'technical-training', "#{slug}.md")
end

def frontmatter_slug(text)
  head = text.split(/^---\s*$/)[1].to_s
  m = head.match(/^slug:\s*["']?([^"'\s]+)["']?\s*$/)
  m && m[1]
end

# The body of the "## Course links" section, or nil when the page has none.
def course_links_section(text)
  m = text.match(/^##\s+Course links\s*$(.*?)(?=^##\s|\z)/m)
  m && m[1]
end

def related_modules_line(section)
  return nil if section.nil?

  section.lines.find { |line| line =~ /^-\s+\*{0,2}Related modules?\*{0,2}:/ }
end

def modules_in_line(line)
  line.to_s.scan(%r{/modules/(module\d{2})/}).flatten.uniq
end

track_modules = Array(track['modules'])

track_modules.each do |entry|
  slug = entry['slug']
  next if slug.nil?

  path = unit_page_path(ROOT, slug)
  unless File.exist?(path)
    warnings << "[WARN] #{slug}: technical_track.yml lists a unit with no page at technical-training/#{slug}.md"
    next
  end

  text = File.read(path, encoding: 'UTF-8')
  page_slug = frontmatter_slug(text)
  if page_slug != slug
    warnings << "[WARN] #{slug}: page front matter slug is #{page_slug.inspect}; the capability brief include matches on page.slug"
  end

  expected = Array(entry['mapped_modules']).compact.uniq
  section = course_links_section(text)
  line = related_modules_line(section)
  found = modules_in_line(line)

  if expected.empty?
    unless found.empty?
      warnings << "[WARN] #{slug}: page Course links name #{found.inspect} but technical_track.yml maps no modules to this unit"
    end
    next
  end

  if section.nil?
    warnings << "[WARN] #{slug}: page has no '## Course links' section, but technical_track.yml maps #{expected.inspect}"
    next
  end

  if line.nil?
    warnings << "[WARN] #{slug}: Course links has no 'Related module(s):' line, but technical_track.yml maps #{expected.inspect}"
    next
  end

  if found.sort != expected.sort
    warnings << "[WARN] #{slug}: Course links name #{found.sort.inspect} but technical_track.yml maps #{expected.sort.inspect}"
  end

  plural = line =~ /Related modules:/ ? true : false
  if plural != (expected.size > 1)
    want = expected.size > 1 ? 'Related modules:' : 'Related module:'
    warnings << "[WARN] #{slug}: Course links label should read '#{want}' for #{expected.size} module(s)"
  end
end

# ---------------------------------------------------------------------------
# technical_capabilities.yml has to describe exactly the units that exist.
# `_includes/ui/technical-capability-brief.html` looks an entry up by page.slug,
# so an entry with no page renders nowhere and a page with no entry loses its
# capability brief without any build error.

if File.exist?(capabilities_path)
  capabilities = YAML.safe_load(File.read(capabilities_path, encoding: 'UTF-8'), permitted_classes: [Date], aliases: true) || {}
  cap_slugs = Array(capabilities['units']).map { |u| u['slug'] }.compact

  duplicates = cap_slugs.tally.select { |_, n| n > 1 }.keys
  duplicates.each { |slug| warnings << "[WARN] technical_capabilities.yml has duplicate entries for #{slug}" }

  cap_slugs.uniq.each do |slug|
    path = unit_page_path(ROOT, slug)
    unless File.exist?(path)
      warnings << "[WARN] technical_capabilities.yml entry '#{slug}' has no unit page at technical-training/#{slug}.md"
      next
    end

    page_slug = frontmatter_slug(File.read(path, encoding: 'UTF-8'))
    if page_slug != slug
      warnings << "[WARN] technical_capabilities.yml entry '#{slug}' does not match that page's front matter slug #{page_slug.inspect}"
    end
  end

  (track_slugs - cap_slugs).each do |slug|
    warnings << "[WARN] technical_capabilities.yml has no entry for technical unit '#{slug}'"
  end
  (cap_slugs.uniq - track_slugs).each do |slug|
    warnings << "[WARN] technical_capabilities.yml entry '#{slug}' is not a unit in technical_track.yml"
  end
else
  warnings << '[WARN] Missing _data/technical_capabilities.yml.'
end

puts "Technical evidence validation complete (#{warnings.empty? ? 'no warnings' : 'warnings below'})."
warnings.each { |w| puts w }
exit(warnings.empty? ? 0 : 1)
