#!/usr/bin/env ruby
# frozen_string_literal: true

require 'set'

ROOT = File.expand_path('..', __dir__)
SITE = File.join(ROOT, '_site')

unless Dir.exist?(SITE)
  warn "[ERROR] _site not found. Run `bundle exec jekyll build` first."
  exit 1
end

html_files = Dir.glob(File.join(SITE, '**', '*.html'))
missing = []
checked = Set.new

def candidate_paths(site_root, path)
  clean = path.split('#', 2).first.split('?', 2).first
  return [] if clean.nil? || clean.empty?

  clean = clean.sub(%r{^/}, '')
  direct = File.join(site_root, clean)
  [
    direct,
    "#{direct}.html",
    File.join(direct, 'index.html')
  ].uniq
end

html_files.each do |file|
  content = File.read(file)
  links = content.scan(/(?:href|src)=["']([^"']+)["']/i).flatten
  links.each do |href|
    next if href.start_with?('http://', 'https://', 'mailto:', 'tel:', 'javascript:', 'data:')
    next if href.start_with?('#')
    next unless href.start_with?('/')

    key = "#{file}|#{href}"
    next if checked.include?(key)

    checked << key
    ok = candidate_paths(SITE, href).any? { |p| File.exist?(p) }
    missing << [file.sub("#{SITE}/", ''), href] unless ok
  end
end

if missing.empty?
  puts 'Site link audit complete: no missing internal links.'
  exit 0
end

puts "Site link audit found #{missing.size} missing internal links:"
missing.each { |from, href| puts "- #{from} -> #{href}" }
exit 1
