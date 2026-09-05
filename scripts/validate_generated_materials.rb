#!/usr/bin/env ruby
# frozen_string_literal: true

# Guard the generated teaching materials and the Marp deck sources.
#
# Three regressions this catches, all of which shipped to learners before:
#
#   1. Empty rubrics. `rubric_lines` selected only top-level bullets, so a two-level
#      rubric ("- **Minimum pass**" with indented criteria beneath) lost every
#      criterion. All 25 worksheets told learners to score themselves against three
#      bare headings.
#   2. Raw Liquid and kramdown attribute lists leaking into files Jekyll never
#      renders. Worksheets have no front matter, so `{{ '/x/' | relative_url }}`
#      reached the reader verbatim, and a mis-anchored regex printed
#      "**Scenario:** {: #studio-activity}" as the scenario for four modules.
#   3. Decks with no theme and slides with no body. The ten technical-unit decks
#      declared no theme at all, and two committed decks carried an empty slide.
#
# Run from the repository root. Exits non-zero when it finds a problem.

require "pathname"

ROOT = Pathname.new(__dir__).parent
problems = []

def read(path) = path.read(encoding: "UTF-8")

# ---------------------------------------------------------------- worksheets
worksheets = ROOT.glob("assets/worksheets/module*/*-activity.md").sort
problems << "no worksheets found under assets/worksheets/" if worksheets.empty?

worksheets.each do |path|
  rel = path.relative_path_from(ROOT)
  text = read(path)

  text.scan(/\{\{.*?\}\}|\{%.*?%\}/m).each do |liquid|
    problems << "#{rel}: unrendered Liquid reaches the reader: #{liquid.strip[0, 70]}"
  end
  text.scan(/^\s*\{:\s*#/).each do
    problems << "#{rel}: a kramdown attribute list was captured as content"
  end

  # Every worksheet must carry a rubric whose tiers actually say something. Two forms
  # are in use and both are fine: the tier label can carry its criteria inline after a
  # colon, or as indented bullets beneath it. What the generator used to emit was
  # neither — three bare tier labels and nothing else, so learners were told to score
  # themselves against "Minimum pass / Strong performance / Common failure modes".
  section = text[/^#+\s*(?:Assessment\s+)?[Rr]ubric.*?(?=^#+\s|\z)/m]
  if section.nil?
    problems << "#{rel}: no rubric section"
  else
    lines = section.lines
    first = lines.index { |l| l.match?(/^-\s+\*\*/) }
    if first.nil?
      problems << "#{rel}: rubric section has no tier labels"
    else
      block = lines[first..].take_while { |l| l.match?(/^-\s|^\s+[-*]\s|^\s*$/) }
      block.each_with_index do |line, i|
        next unless line.match?(/^-\s+\*\*/)

        inline = line.sub(/^-\s+\*\*.*?\*\*:?/, "").strip
        nested = block[(i + 1)..].to_a
                      .take_while { |l| !l.match?(/^-\s+\*\*/) }
                      .count { |l| l.match?(/^\s+[-*]\s+\S/) }
        next if inline.length > 20 || nested.positive?

        problems << "#{rel}: rubric tier #{line.strip[0, 40]} has no criteria, inline or nested"
      end
    end
  end
end

# ------------------------------------------------------------- session kits
ROOT.glob("teaching/sessions/module*.md").sort.each do |path|
  rel = path.relative_path_from(ROOT)
  read(path).scan(/^\s*\{:\s*#/).each do
    problems << "#{rel}: a kramdown attribute list was captured as content"
  end
end

# -------------------------------------------------------------- Marp decks
ROOT.glob("course/decks/marp/**/*.marp.md").sort.each do |path|
  rel  = path.relative_path_from(ROOT)
  text = read(path)

  front = text[/\A---\n(.*?)\n---\n/m, 1]
  if front.nil?
    problems << "#{rel}: no front matter"
    next
  end
  problems << "#{rel}: declares no theme" unless front.match?(/^theme:\s*\S/)

  # Slides are separated by a --- rule; a slide whose only content is its heading
  # (or nothing at all) is a placeholder that was committed by accident.
  body = text.sub(/\A---\n.*?\n---\n/m, "")
  body.split(/^---\s*$/).each_with_index do |slide, index|
    stripped = slide.lines.reject { |l| l.strip.empty? || l.strip.start_with?("<!--") }
    next if stripped.empty? && index.zero?
    headings, rest = stripped.partition { |l| l.strip.start_with?("#") }
    next unless headings.any? && rest.empty?

    problems << "#{rel}: slide #{index + 1} (#{headings.first.strip[0, 60]}) has a heading and no body"
  end
end

if problems.empty?
  counts = [
    "#{worksheets.size} worksheets",
    "#{ROOT.glob('teaching/sessions/module*.md').size} session kits",
    "#{ROOT.glob('course/decks/marp/**/*.marp.md').size} deck sources"
  ]
  puts "OK: #{counts.join(', ')} — rubrics populated, no leaked Liquid, every deck themed with no empty slides"
  exit 0
end

warn "Generated-material validation found #{problems.size} problem(s):"
problems.first(60).each { |p| warn "  #{p}" }
warn "  ... and #{problems.size - 60} more" if problems.size > 60
exit 1
