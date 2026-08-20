#!/usr/bin/env ruby
# frozen_string_literal: true

# Audits cross-page fragment links (href="/some/page/#some-anchor") in the built
# site, confirming the target page exists and actually contains that id.
#
# scripts/check_site_links.rb checks that link targets resolve to a page. It does
# not look at fragments, so a heading rename silently breaks every deep link into
# that page — which is exactly what happened when the technical-training units
# were rewritten and their "Quick activity" sections became "Lab: ..." sections.
#
# Run after `jekyll build`. Exits non-zero when a fragment is missing.

require 'pathname'
require 'set'

ROOT = Pathname.new(File.expand_path('..', __dir__))
SITE = ROOT.join('_site')

unless SITE.directory?
  warn '[ERROR] _site not found. Run `bundle exec jekyll build` first.'
  exit 1
end

def target_file(site, page)
  rel = page.sub(%r{\A/}, '').sub(%r{/\z}, '')
  candidates = [site.join(rel, 'index.html'), site.join(rel)]
  candidates.find { |c| c.file? }
end

ids_cache = {}
def ids_for(path, cache)
  cache[path] ||= path.read(encoding: 'UTF-8').scan(/\sid="([^"]+)"/).flatten.to_set
end

missing = []
checked = 0

Dir.glob(SITE.join('**', '*.html')).sort.each do |file|
  source = Pathname.new(file)
  html = source.read(encoding: 'UTF-8')

  html.scan(/href="(\/[^"#]*)#([^"]+)"/) do |page, anchor|
    next if anchor.start_with?('/')

    checked += 1
    target = target_file(SITE, page)
    next if target.nil? # page-level breakage is check_site_links.rb's job

    next if ids_for(target, ids_cache).include?(anchor)

    missing << {
      from: source.relative_path_from(SITE).to_s,
      link: "#{page}##{anchor}"
    }
  end
end

puts "Anchor audit from #{SITE}"
puts "Cross-page fragment links checked: #{checked}"

if missing.empty?
  puts 'No broken fragment links found.'
  exit 0
end

distinct = missing.uniq { |m| m[:link] }
puts "Found #{distinct.size} broken fragment link(s):"
distinct.each { |m| puts "- #{m[:from]} -> #{m[:link]}" }
exit 1
