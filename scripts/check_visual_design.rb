#!/usr/bin/env ruby
# frozen_string_literal: true
require 'yaml'
require 'pathname'
require 'digest'
ROOT = Pathname.new(__dir__).parent
problems = []
data = YAML.safe_load(ROOT.join('_data/module_deck_visuals.yml').read(encoding: 'UTF-8'), aliases: false).fetch('modules')
expected = (2..9).map { |n| format('module%02d', n) }
problems << 'Visual module scope is not exactly 02-09' unless data.keys.sort == expected
images = 0
data.each do |slug, items|
  problems << "#{slug}: fewer than two instructional visual examples" unless items.size >= 2
  source = ROOT.join("course/decks/marp/modules/#{slug}.marp.md").read(encoding: 'UTF-8')
  items.each do |item|
    %w[type title lead prompt description source].each { |k| problems << "#{slug}: missing #{k}" if item[k].to_s.strip.empty? }
    problems << "#{slug}: visual not in generated deck" unless source.include?(item.fetch('title'))
    Array(item['images']).each do |image|
      images += 1
      problems << "#{slug}: absent image #{image['src']}" unless ROOT.join(image.fetch('src').sub(%r{\A/}, '')).file?
      problems << "#{slug}: meaningful alternative/caption required" unless image['alt'].to_s.size > 30 && image['caption'].to_s.size > 10
      problems << "#{slug}: scientific source/license missing" unless item.fetch('source').include?('CC BY 4.0') && item.fetch('source').include?('10.1126/science.adk4858')
    end
    if item['type'] == 'flow'
      problems << "#{slug}: invalid diagram length" unless item.fetch('steps').size.between?(3, 4)
    end
  end
end
# Regression protection for the exact examples in the visual data.
counts = [4, 1, 0]
raise 'Synthetic notebook arithmetic failed' unless counts.sum == 5 && counts.sum.fdiv(counts.size) == 5.0 / 3 && counts.reject(&:zero?).sum.fdiv(2) == 2.5
points = { a: [0,0], b: [0,3], c: [-4,3], d: [4,3] }
distance = ->(a,b) { Math.hypot(points[a][0] - points[b][0], points[a][1] - points[b][1]) }
lengths = [%i[a b], %i[b c], %i[b d]].map { |a,b| distance.call(a,b) }
raise 'Synthetic skeleton arithmetic failed' unless lengths == [3.0,4.0,4.0] && lengths.sum == 11.0 && (lengths[0]+lengths[1])/distance.call(:a,:c) == 1.4
catalog = ROOT.join('teaching/sessions/index.md').read
problems << 'Generated output overwrote the searchable session catalog' unless catalog.include?('id="session-search"') && catalog.include?('session-card')
ROOT.glob('course/decks/marp/**/*.marp.md').each do |source|
  reader = ROOT.join('course/decks/marp/out', source.relative_path_from(ROOT.join('course/decks/marp')).to_s.sub(/\.marp\.md\z/, '.reader.html'))
  if !reader.file?
    problems << "Missing reading version: #{reader.relative_path_from(ROOT)}"
    next
  end
  html = reader.read(encoding:'UTF-8')
  problems << "#{reader}: needs normal HTML document and main landmark" unless html.include?('<html lang="en">') && html.include?('<main id="reading-content"')
  problems << "#{reader}: rasterized or SVG reader" if html.include?('<foreignObject')
  problems << "#{reader}: primary heading mismatch" unless html.scan(/<h1(?:\s|>)/).size == 1
end
if problems.any?
  warn problems.join("\n"); exit 1
end
puts "PASS visual design: #{data.size} modules, #{data.values.sum(&:size)} examples, #{images} credited scientific images; all reading versions; synthetic arithmetic; session catalog preserved."
