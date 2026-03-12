#!/usr/bin/env ruby
# frozen_string_literal: true

require 'yaml'
require 'date'

ROOT = File.expand_path('..', __dir__)
track_path = File.join(ROOT, '_data', 'technical_track.yml')
evidence_path = File.join(ROOT, '_data', 'technical_evidence.yml')

unless File.exist?(track_path) && File.exist?(evidence_path)
  warn '[WARN] Missing technical track or technical evidence data file.'
  exit 0
end

track = YAML.safe_load(File.read(track_path), permitted_classes: [Date], aliases: true) || {}
evidence = YAML.safe_load(File.read(evidence_path), permitted_classes: [Date], aliases: true) || {}

track_slugs = Array(track['modules']).map { |m| m['slug'] }.compact
unit_entries = Array(evidence['units'])
unit_by_slug = unit_entries.each_with_object({}) { |u, h| h[u['slug']] = u }

paper_lib = (evidence.dig('library', 'papers') || {}).keys
dataset_lib = (evidence.dig('library', 'datasets') || {}).keys

warnings = []

track_slugs.each do |slug|
  unit = unit_by_slug[slug]
  if unit.nil?
    warnings << "[WARN] missing evidence entry for technical unit slug: #{slug}"
    next
  end

  papers = Array(unit['papers'])
  datasets = Array(unit['datasets'])
  checks = Array(unit['competency_checks'])

  warnings << "[WARN] #{slug}: fewer than 2 key papers" if papers.size < 2
  warnings << "[WARN] #{slug}: missing key dataset anchors" if datasets.empty?
  warnings << "[WARN] #{slug}: missing competency checks" if checks.empty?

  papers.each do |pid|
    warnings << "[WARN] #{slug}: unknown paper id '#{pid}'" unless paper_lib.include?(pid)
  end
  datasets.each do |did|
    warnings << "[WARN] #{slug}: unknown dataset id '#{did}'" unless dataset_lib.include?(did)
  end
end

extra = unit_by_slug.keys - track_slugs
extra.each { |slug| warnings << "[WARN] evidence entry has no matching technical unit: #{slug}" }

puts "Technical evidence validation complete (#{warnings.empty? ? 'no warnings' : 'warnings below'})."
warnings.each { |w| puts w }
