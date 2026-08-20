#!/usr/bin/env ruby
# frozen_string_literal: true

# Fail the build when a Marp source has changed without the deck being re-rendered.
#
# The published decks under course/decks/marp/out/ are what instructors actually
# open. In August 2026, 29 of 35 of them were stale: the sources had been
# regenerated and the outputs had not, so every "Open deck" link served content
# that no longer matched its module page. Nothing caught it because mtimes do
# not survive a git clone, which makes "is the output older than the source?"
# unanswerable in CI.
#
# So render_marp.sh records the SHA-256 of each source at render time, and this
# compares the live sources against that record.
#
# When this fails, the fix is to re-render, not to edit the manifest:
#     ./scripts/render_marp.sh

require "digest"
require "json"
require "pathname"

ROOT = Pathname.new(__dir__).parent
SRC_DIR = ROOT.join("course/decks/marp")
OUT_DIR = SRC_DIR.join("out")
MANIFEST = OUT_DIR.join(".render-manifest.json")

unless MANIFEST.exist?
  warn "No render manifest at #{MANIFEST.relative_path_from(ROOT)}."
  warn "Run ./scripts/render_marp.sh to render the decks and create it."
  exit 1
end

recorded = begin
  JSON.parse(MANIFEST.read(encoding: "UTF-8")).fetch("sources", {})
rescue JSON::ParserError => e
  warn "Render manifest is not valid JSON: #{e.message}"
  exit 1
end

live = {}
SRC_DIR.glob("**/*.marp.md").sort.each do |path|
  live[path.relative_path_from(SRC_DIR).to_s] = Digest::SHA256.hexdigest(path.binread)
end

stale   = live.select { |rel, sha| recorded.key?(rel) && recorded[rel] != sha }.keys
added   = live.keys - recorded.keys
removed = recorded.keys - live.keys

# A source with no rendered HTML beside it is stale whatever the manifest says.
missing = live.keys.reject do |rel|
  OUT_DIR.join(rel.sub(/\.marp\.md\z/, ".html")).exist?
end

problems = []
problems << "changed since last render: #{stale.join(', ')}" unless stale.empty?
problems << "added but never rendered: #{added.join(', ')}" unless added.empty?
problems << "rendered output with no source: #{removed.join(', ')}" unless removed.empty?
problems << "no rendered HTML found for: #{missing.join(', ')}" unless missing.empty?

if problems.empty?
  puts "OK: all #{live.size} Marp decks are rendered from their current sources"
  exit 0
end

warn "Published decks are out of date with their sources:"
problems.each { |p| warn "  - #{p}" }
warn ""
warn "Re-render with: ./scripts/render_marp.sh"
exit 1
