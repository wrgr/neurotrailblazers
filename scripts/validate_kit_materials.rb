#!/usr/bin/env ruby
# frozen_string_literal: true

# Fail the build when a teaching kit names material the site does not publish.
#
# Why. The session kits for Modules 03-07 and 09-11 told learners to open "the
# provided" sample CSV, patch set, notebook or metric script, and none of those
# files existed. Both syllabus maps had to route around them (NEXT_CONTENT_PASS.md
# item 5; inventory in docs/reviews/2026-09-kit-materials-audit.md). The link audit
# could not see the problem, because there was no link to check: the materials were
# named in prose. This gate checks both halves.
#
# Scope: modules/*.md, teaching/sessions/*.md, assets/worksheets/**/*.md and the kit
# READMEs under assets/kits/. Three rules:
#
#   1. Every site path these files reference must resolve. That covers
#      {{ '/x' | relative_url }} and absolute_url filters, Markdown links and
#      href/src attributes to "/..." paths, bare /assets/... and /notebooks/... paths
#      anywhere in the text (including code spans), relative links inside kit
#      READMEs, and the path-valued front-matter keys of module pages (slides,
#      notebook, downloads, image, datasets, related_tools). A path with a file
#      extension must exist on disk; a page path must match a declared permalink or
#      a source file. Paths containing a placeholder (NN, <name>) are skipped.
#
#   2. A sentence that names material as supplied must say where it is. A line that
#      contains one of the trigger phrases below fails unless the same line carries a
#      link or /assets/ path that rule 1 resolves. Triggers: "provided" (not
#      "provided that"), "supplied", "pre-loaded", "course portal", "course dataset",
#      "practice dataset", "shared dataset", "pre-identified", "pre-computed", and
#      "sample" followed by notebook, file, CSV, patch(es), image(s), dataset or data.
#      These are the phrasings the broken kits used. The rule is per line because
#      every module page writes one list item or one paragraph per line; if that
#      changes, widen the unit here rather than loosening the phrases.
#      "Precomputed" as a Neuroglancer format name is not a trigger (hyphen required).
#
#   3. assets/kits/manifest.json lists every file under assets/kits/ with its
#      SHA-256, and nothing else. A kit file edited by hand, added without the
#      generator, or deleted fails here. Regenerate with
#      `ruby scripts/generate_kit_materials.rb`, which rewrites the manifest.
#
# Stdlib only. Run from the repository root. Exits non-zero on any problem.

require 'digest'
require 'json'
require 'set'
require 'yaml'
require 'date'

ROOT = File.expand_path('..', __dir__)
SKIP_PREFIXES = %w[vendor/ _site/ node_modules/ .git/ .chrome].freeze

SCOPE = (Dir.glob(File.join(ROOT, 'modules', 'module*.md')) +
         Dir.glob(File.join(ROOT, 'teaching', 'sessions', '*.md')) +
         Dir.glob(File.join(ROOT, 'assets', 'worksheets', '**', '*.md')) +
         Dir.glob(File.join(ROOT, 'assets', 'kits', '**', '*.md'))).sort.freeze

PLACEHOLDER = /NN|<[^>]+>|\{\{|\{%/.freeze
FRONT_MATTER_KEYS = %w[slides notebook downloads image datasets related_tools].freeze

TRIGGER = /
  \bprovided\b(?!\s+that)
  | \bsupplied\b
  | \bpre-loaded\b
  | \bcourse\s+portal\b
  | \bcourse\s+dataset\b
  | \bpractice\s+dataset\b
  | \bshared\s+dataset\b
  | \bpre-identified\b
  | \bpre-computed\b
  | \bsample\s+(?:notebooks?|files?|csv|patch(?:es)?|images?|datasets?|data)\b
/ix.freeze

def rel(path) = path.sub("#{ROOT}/", '')

def permalinks
  files = Dir.glob(File.join(ROOT, '**', '*.{md,html}')).reject do |p|
    SKIP_PREFIXES.any? { |s| rel(p).start_with?(s) }
  end
  set = Set.new
  files.each do |file|
    head = File.read(file, encoding: 'UTF-8')[0, 4000].to_s
    head.scan(/^permalink:\s*["']?([^"'\n]+?)["']?\s*$/) { |m| set << m[0].strip }
  end
  set
end

PERMALINKS = permalinks

# Resolves a site path ("/x/y/", "/assets/a.csv") or, when `base` is given, a path
# relative to the directory of the file that links it.
def resolves?(url, base: nil)
  path = url.sub(/[?#].*\z/, '')
  return true if path.empty?

  unless path.start_with?('/')
    return false unless base

    return File.exist?(File.expand_path(path, base))
  end
  return true if PERMALINKS.include?(path) || PERMALINKS.include?("#{path.chomp('/')}/")

  local = path.sub(%r{\A/}, '')
  return File.file?(File.join(ROOT, local)) if File.extname(local) != '' && !local.end_with?('/')

  stem = local.chomp('/')
  return false if stem.empty?

  [stem, "#{stem}.md", "#{stem}.html", "#{stem}/index.md", "#{stem}/index.html"]
    .any? { |c| File.exist?(File.join(ROOT, c)) }
end

# Every site path a line references, with whether it is relative to the file.
def references(line)
  refs = []
  line.scan(/\{\{\s*['"]([^'"]+)['"]\s*\|\s*(?:relative_url|absolute_url)\s*\}\}/) { |m| refs << m[0] }
  line.scan(/\]\(([^)\s]+)(?:\s+"[^"]*")?\)/) do |m|
    target = m[0]
    next if target.start_with?('{{') # handled above
    next if target.match?(%r{\A(?:[a-z]+:|//|#)}i)

    refs << target
  end
  line.scan(/(?:href|src)=["']([^"']+)["']/) do |m|
    target = m[0]
    next if target.start_with?('{{') || target.match?(%r{\A(?:[a-z]+:|//|#)}i)

    refs << target
  end
  line.scan(%r{(?<![\w.:/'"(])(/(?:assets|notebooks)/[A-Za-z0-9_.\-/]+[A-Za-z0-9_/])}) { |m| refs << m[0] }
  refs.uniq.reject { |r| r.match?(PLACEHOLDER) }
end

problems = []

SCOPE.each do |file|
  text = File.read(file, encoding: 'UTF-8')
  # Only kit READMEs use file-relative links; elsewhere a relative target is not a
  # site path this gate can judge, so it is left to the link audit.
  base = rel(file).start_with?('assets/kits/') ? File.dirname(file) : nil
  in_fence = false
  text.each_line.with_index(1) do |line, lineno|
    in_fence = !in_fence if line.lstrip.start_with?('```')
    refs = in_fence ? [] : references(line).select { |r| r.start_with?('/') || base }
    resolved = refs.select do |r|
      ok = resolves?(r, base: base)
      problems << "#{rel(file)}:#{lineno}: #{r} does not resolve" unless ok
      ok
    end
    next if in_fence

    trigger = line.match(TRIGGER)
    next unless trigger
    next if resolved.any?

    problems << "#{rel(file)}:#{lineno}: names material as \"#{trigger[0]}\" but links nothing that resolves"
  end
end

# Front-matter paths on module pages.
Dir.glob(File.join(ROOT, 'modules', 'module*.md')).sort.each do |file|
  parts = File.read(file, encoding: 'UTF-8').split(/^---\s*$\n/, 3)
  next if parts.length < 3

  fm = YAML.safe_load(parts[1], permitted_classes: [Date], aliases: true) || {}
  FRONT_MATTER_KEYS.each do |key|
    Array(fm[key]).each do |value|
      next unless value.is_a?(String) && value.start_with?('/')
      next if resolves?(value)

      problems << "#{rel(file)}: front matter #{key}: #{value} does not resolve"
    end
  end
end

# Manifest.
manifest_path = File.join(ROOT, 'assets', 'kits', 'manifest.json')
if File.exist?(manifest_path)
  listed = JSON.parse(File.read(manifest_path, encoding: 'UTF-8')).fetch('files', [])
  on_disk = Dir.glob(File.join(ROOT, 'assets', 'kits', '**', '*'))
               .select { |f| File.file?(f) }
               .map { |f| rel(f) }
               .reject { |f| f == 'assets/kits/manifest.json' }
               .to_set
  listed.each do |entry|
    path = entry['path']
    full = File.join(ROOT, path)
    if !File.file?(full)
      problems << "assets/kits/manifest.json lists #{path}, which does not exist"
    elsif Digest::SHA256.file(full).hexdigest != entry['sha256']
      problems << "#{path} differs from its manifest checksum; regenerate with ruby scripts/generate_kit_materials.rb"
    end
  end
  (on_disk - listed.map { |e| e['path'] }).sort.each do |path|
    problems << "#{path} is not in assets/kits/manifest.json; add it through scripts/generate_kit_materials.rb"
  end
elsif Dir.exist?(File.join(ROOT, 'assets', 'kits'))
  problems << 'assets/kits/ exists but assets/kits/manifest.json does not'
end

if problems.empty?
  puts "OK: every kit material resolves (#{SCOPE.size} files scanned, #{PERMALINKS.size} permalinks indexed, " \
       'manifest checksums match).'
  exit 0
end

warn "Kit material problems (#{problems.size}):"
problems.each { |p| warn "  - #{p}" }
exit 1
