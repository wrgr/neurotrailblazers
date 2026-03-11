#!/usr/bin/env ruby
# frozen_string_literal: true

require 'fileutils'
require 'set'

ROOT = File.expand_path('..', __dir__)
DEFAULT_SOURCE_ROOT = '/Users/wgray13/Downloads/nt_figure_extraction_package (1)'
source_root = ENV.fetch('NT_FIG_ROOT', DEFAULT_SOURCE_ROOT)

unless Dir.exist?(source_root)
  warn "Source root not found: #{source_root}"
  exit 1
end

deck_dir = File.join(ROOT, 'course/decks')
asset_root = File.join(ROOT, 'assets/images/technical-training')
fig_id_regex = /FIG-[A-Z0-9_\-]+-S\d{2}-\d{2}/

copied = []
missing = []

Dir.glob(File.join(deck_dir, '*.md')).sort.each do |deck_path|
  slug = File.basename(deck_path, '.md')
  ids = File.read(deck_path).scan(fig_id_regex).uniq
  next if ids.empty?

  target_dir = File.join(asset_root, slug)
  FileUtils.mkdir_p(target_dir)

  ids.each do |id|
    target = File.join(target_dir, "#{id}.png")
    next if File.exist?(target)

    matches = Dir.glob(File.join(source_root, '**', "#{id}.png"))
    if matches.empty?
      missing << [slug, id]
      next
    end

    FileUtils.cp(matches.first, target)
    copied << [slug, id, matches.first]
  end
end

puts "Deck figure import from: #{source_root}"
puts "Copied: #{copied.size}"
puts "Missing: #{missing.size}"

if copied.any?
  puts "\nCopied figures:"
  copied.each do |slug, id, src|
    puts "- #{slug}: #{id} <= #{src}"
  end
end

if missing.any?
  puts "\nStill missing figures:"
  missing.each do |slug, id|
    puts "- #{slug}: #{id}"
  end
end

exit 0
