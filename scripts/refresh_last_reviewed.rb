#!/usr/bin/env ruby
# frozen_string_literal: true

# Sets `last_reviewed` in the front matter of every page that already carries the
# field to the date of the file's most recent commit, so the "Last reviewed" line
# the layout renders (_includes/ui/page-nav.html) tracks git history instead of a
# hand-typed date.
#
#   ruby scripts/refresh_last_reviewed.rb            # rewrite dates that differ
#   ruby scripts/refresh_last_reviewed.rb --check    # report only, exit 1 if stale
#
# The date is `git log -1 --format=%cs -- <file>`, the commit date of the last
# change to the file. Uncommitted edits do not move it: a page edited today shows
# its previous commit date until that edit is committed, and the next run after the
# commit brings it forward. A file with no commit yet is left alone. Pages that do
# not have the field are not given one; add `last_reviewed:` by hand when a page
# should show the line.

require "pathname"
require "shellwords"

ROOT = Pathname.new(__dir__).parent
CHECK_ONLY = ARGV.include?("--check")

SKIP_PREFIXES = %w[_site/ node_modules/ vendor/ docs/ data/ .build-cs/].freeze

def tracked_pages
  Dir.chdir(ROOT) do
    `git ls-files -- '*.md' '*.html'`.split("\n")
  end.reject { |rel| SKIP_PREFIXES.any? { |p| rel.start_with?(p) } }
end

def front_matter_span(text)
  return nil unless text.start_with?("---")

  close = text.index(/^---\s*$/, 3)
  close ? [0, close] : nil
end

def last_commit_date(rel)
  Dir.chdir(ROOT) { `git log -1 --format=%cs -- #{rel.shellescape}`.strip }
end

changed = []
stale = []
unchanged = 0
tracked_pages.each do |rel|
  path = ROOT.join(rel)
  text = path.read(encoding: "UTF-8")
  span = front_matter_span(text)
  next unless span

  head = text[span[0]...span[1]]
  match = head.match(/^last_reviewed:[ \t]*["']?(\d{4}-\d{2}-\d{2})?["']?[ \t]*$/)
  next unless match

  date = last_commit_date(rel)
  next if date.empty?

  if match[1] == date
    unchanged += 1
    next
  end

  stale << "#{rel}: #{match[1] || '(blank)'} -> #{date}"
  next if CHECK_ONLY

  new_head = head.sub(/^last_reviewed:.*$/, "last_reviewed: #{date}")
  path.write(new_head + text[span[1]..], encoding: "UTF-8")
  changed << rel
end

puts stale
if CHECK_ONLY
  puts "#{stale.size} stale, #{unchanged} current."
  exit(stale.empty? ? 0 : 1)
else
  puts "Updated #{changed.size} page(s); #{unchanged} already current."
end
