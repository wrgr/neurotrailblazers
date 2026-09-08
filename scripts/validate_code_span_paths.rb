#!/usr/bin/env ruby
# frozen_string_literal: true

# Fail the build when a site path written inside a backtick code span does not
# resolve to a page.
#
# check_site_links.rb only scans href= and src= attributes, so a path written as
# prose-with-monospace slips past it. That is not hypothetical: when the 25
# modules/slides/moduleNN pages were deleted (NEXT_CONTENT_PASS.md 3.1), all 25
# worksheet footers still cited `/modules/slides/moduleNN/` in a code span. The
# link audit passed; the paths were dead. They were found by grep, which is not a
# gate.
#
# Scope is deliberately narrow to keep false positives at zero: only strings that
# both start and end with "/" are treated as site URLs. A repo path in a code span
# (`scripts/foo.rb`, `_data/journal_papers.yml`) has no leading slash and is
# ignored; a file reference like `/assets/x.svg` has no trailing slash and is
# ignored too, because check_figure_refs and the link audit already cover assets.

require 'set'

ROOT = File.expand_path('..', __dir__)

SKIP_PREFIXES = %w[vendor/ _site/ node_modules/ docs/ .git/ .chrome].freeze
SOURCE_GLOBS = ['**/*.md', '**/*.html'].freeze

# Paths that are documented as patterns rather than real URLs.
PLACEHOLDER = /NN|<[^>]+>|:[a-z_]+/.freeze

def source_files
  SOURCE_GLOBS.flat_map { |g| Dir.glob(File.join(ROOT, g)) }.reject do |path|
    rel = path.sub("#{ROOT}/", '')
    SKIP_PREFIXES.any? { |p| rel.start_with?(p) }
  end.sort.uniq
end

# Every permalink declared in front matter, which is how most pages here define
# their URL; a path-derived page has no permalink and is matched on disk instead.
def permalinks(files)
  set = Set.new
  files.each do |file|
    head = File.read(file, encoding: 'UTF-8')[0, 4000].to_s
    head.scan(/^permalink:\s*["']?([^"'\n]+?)["']?\s*$/) { |m| set << m[0].strip }
  end
  set
end

def resolves?(url, perms)
  return true if perms.include?(url)

  rel = url.sub(%r{\A/}, '').sub(%r{/\z}, '')
  return false if rel.empty?

  [rel, "#{rel}.md", "#{rel}.html", "#{rel}/index.md", "#{rel}/index.html"]
    .any? { |c| File.exist?(File.join(ROOT, c)) }
end

files = source_files
perms = permalinks(files)
problems = []

files.each do |file|
  rel_file = file.sub("#{ROOT}/", '')
  content = File.read(file, encoding: 'UTF-8')
  content.each_line.with_index(1) do |line, lineno|
    line.scan(%r{`(/[A-Za-z0-9._~\-/]*/)`}) do |match|
      url = match[0]
      next if url.match?(PLACEHOLDER)
      next if resolves?(url, perms)

      problems << [rel_file, lineno, url]
    end
  end
end

if problems.empty?
  puts "OK: every site path in a code span resolves (#{perms.size} permalinks indexed, " \
       "#{files.size} source files scanned)."
  exit 0
end

puts "Found #{problems.size} site paths in code spans that do not resolve:"
problems.each { |file, lineno, url| puts "- #{file}:#{lineno} -> #{url}" }
puts
puts 'Either fix the path or, if it is deliberately a pattern rather than a URL,'
puts 'write it with an NN/<placeholder> so it is not read as a live link.'
exit 1
