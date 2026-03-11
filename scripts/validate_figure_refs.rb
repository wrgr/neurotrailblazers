#!/usr/bin/env ruby
# frozen_string_literal: true

require 'set'

ROOT = File.expand_path('..', __dir__)
SCAN_GLOBS = [
  'course/decks/*.md',
  'technical-training/*.md',
  'technical-training/slides/*.md'
].freeze
SKIP_PATTERNS = [
  /-candidates\.md$/
].freeze
ASSET_GLOB = File.join(ROOT, 'assets/images/technical-training/**/*.png')
FIG_ID_REGEX = /FIG-[A-Z0-9_\-]+-S\d{2}-\d{2}/
MARP_IMAGE_REGEX = /!\[[^\]]*\]\(([^)]+)\)/

asset_ids = Dir.glob(ASSET_GLOB).map { |p| File.basename(p, '.png') }.to_set

refs_by_file = {}
SCAN_GLOBS.each do |glob|
  Dir.glob(File.join(ROOT, glob)).each do |path|
    next if SKIP_PATTERNS.any? { |pat| path.match?(pat) }

    content = File.read(path)
    ids = content.scan(FIG_ID_REGEX).uniq
    refs_by_file[path] = ids unless ids.empty?
  end
end

missing = {}
refs_by_file.each do |path, ids|
  unresolved = ids.reject { |id| asset_ids.include?(id) }
  missing[path] = unresolved unless unresolved.empty?
end

puts "Figure ref validation from #{ROOT}"
puts "Scanned files: #{refs_by_file.size}"
puts "Available asset IDs: #{asset_ids.size}"

if missing.empty?
  puts 'No missing figure references found.'
  exit 0
end

puts "\nMissing figure references detected:"
missing.sort.each do |path, ids|
  rel = path.delete_prefix("#{ROOT}/")
  puts "- #{rel}"
  ids.sort.each { |id| puts "  - #{id}" }
end

puts "\nValidation complete with warnings."

marp_missing = {}
Dir.glob(File.join(ROOT, 'course/decks/marp/*.marp.md')).each do |path|
  content = File.read(path)
  missing_paths = content.scan(MARP_IMAGE_REGEX).flatten.uniq.each_with_object([]) do |img_ref, acc|
    next if img_ref.start_with?('http://', 'https://')

    candidate = File.expand_path(img_ref, File.dirname(path))
    acc << img_ref unless File.exist?(candidate)
  end
  marp_missing[path] = missing_paths unless missing_paths.empty?
end

if marp_missing.empty?
  puts "\nMarp image path check: no missing local image paths."
else
  puts "\nMarp image path warnings:"
  marp_missing.sort.each do |path, rels|
    rel = path.delete_prefix("#{ROOT}/")
    puts "- #{rel}"
    rels.each { |r| puts "  - #{r}" }
  end
end

puts "\nDone."
exit 0
