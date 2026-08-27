#!/usr/bin/env ruby

require "yaml"
require "pathname"
require "date"

ROOT = Pathname.new(__dir__).parent

CONTENT_GLOBS = [
  "modules/*.md",
  "avatars/*.md",
  "datasets/*.md",
  "tools/*.md",
  "frameworks/*.md",
  "tracks/*.md",
  "concepts/*.md",
  "technical-training/*.md",
  "technical-training/*/*.md",
  "start-here.md",
  "models.md",
  "education/models.md",
  "content-library/*.md",
  "content-library/*/*.md",
  "hidden-curriculum/*.md",
  "teaching/*.md",
  "teaching/sessions/*.md",
  "teaching/lectures/*.md",
  "modules/slides/*.md",
  "core/*.md",
  "modes/*.md",
].freeze

REQUIRED_BY_TYPE = {
  "modules" => %w[title module_number slug short_title pipeline_stage status],
  "avatars" => %w[layout title role permalink slug summary strengths challenges goals recommended_modules recommended_datasets recommended_tools last_reviewed maintainer],
  "datasets" => %w[layout title slug summary modality species scale access_level use_cases recommended_modules related_tools related_frameworks resource_links last_reviewed maintainer],
  "tools" => %w[layout title slug summary use_cases recommended_modules related_datasets last_reviewed maintainer],
  "frameworks" => %w[layout title slug summary framework_type related_modules related_tools last_reviewed maintainer],
}.freeze

MODULE_ASSET_FIELDS = %w[slides notebook downloads].freeze
TRACK_METADATA_PATH_PREFIXES = %w[
  avatars/
  datasets/
  tools/
  tracks/
  concepts/
  technical-training/
].freeze

# The core-with-tracks axis. Every published page declares which layer it
# belongs to, so the distinction is checkable rather than implied:
#
#   core       reference material, consulted rather than worked through
#   path       ordered content that belongs to a track and ends in an artifact
#   delivery   material for whoever runs a session, not for the learner
#   navigation hub pages whose job is to route to one of the above
CONTENT_TYPES = %w[core path delivery navigation].freeze

# Directories where a missing content_type is an error rather than an omission.
# Anything under these is published curriculum and has to declare its layer.
CONTENT_TYPE_REQUIRED_PREFIXES = %w[
  content-library/
  hidden-curriculum/
  technical-training/
  modules/
  teaching/
  tracks/
  core/
  modes/
  datasets/
  tools/
  avatars/
  frameworks/
].freeze

def requires_content_type?(path)
  rel = path.relative_path_from(ROOT).to_s
  return true if rel == "start-here.md"

  CONTENT_TYPE_REQUIRED_PREFIXES.any? { |prefix| rel.start_with?(prefix) }
end

def requires_track_metadata?(path)
  rel = path.relative_path_from(ROOT).to_s
  return true if rel == "start-here.md"
  return false if rel.start_with?("modules/")
  return false if rel.start_with?("technical-training/slides/")
  return false if rel.start_with?("frameworks/")

  TRACK_METADATA_PATH_PREFIXES.any? { |prefix| rel.start_with?(prefix) }
end

def extract_frontmatter(path)
  text = path.read(encoding: 'UTF-8')
  return nil unless text.start_with?("---")

  parts = text.split(/^---\s*$\n?/)
  # parts: ["", "yaml", "content..."] or similar
  yaml = parts[1]
  YAML.safe_load(yaml, permitted_classes: [Date], aliases: true) || {}
rescue Psych::SyntaxError => e
  warn "[YAML ERROR] #{path}: #{e.message}"
  nil
end

def type_for(path)
  rel = path.relative_path_from(ROOT).to_s
  return "frameworks" if rel == "models.md"
  return "frameworks" if rel == "education/models.md"

  path.dirname.basename.to_s
end

def validate_file(path)
  fm = extract_frontmatter(path)
  return if fm.nil?
  return if fm["layout"] == "redirect"

  t = type_for(path)
  required = REQUIRED_BY_TYPE[t] || []
  missing = required.reject { |k| fm.key?(k) }

  problems = []

  problems << "missing required keys: #{missing.join(', ')}" unless missing.empty?

  if t == "modules"
    return if path.basename.to_s == "index.md"

    num = fm["module_number"]
    problems << "module_number not an Integer (#{num.inspect})" unless num.is_a?(Integer)
    slug = fm["slug"]
    expected_slug = path.basename(".md").to_s
    problems << "slug '#{slug}' does not match filename '#{expected_slug}'" if slug && slug != expected_slug

    MODULE_ASSET_FIELDS.each do |field|
      next unless fm.key?(field)

      values = fm[field]
      unless values.is_a?(Array)
        problems << "#{field} should be an Array"
        next
      end

      values.each do |raw|
        next unless raw.is_a?(String)
        next if raw.start_with?("http://", "https://")

        unless raw.start_with?("/")
          problems << "#{field} entry should start with '/' or be an absolute URL: #{raw}"
          next
        end

        local_path = ROOT.join(raw.delete_prefix("/"))
        problems << "#{field} entry points to missing file: #{raw}" unless local_path.exist?
      end
    end
  end

  if %w[avatars datasets tools].include?(t)
    return if %w[avatars tools].include?(t) && path.basename.to_s == "index.md"

    slug = fm["slug"]
    expected_slug = path.basename(".md").to_s
    problems << "slug '#{slug}' does not match filename '#{expected_slug}'" if slug && slug != expected_slug
  end

  # An image key is optional, but a declared path has to resolve — 93 phantom
  # image declarations accumulated before this check existed.
  if fm["image"].is_a?(String) && fm["image"].start_with?("/")
    problems << "image points to missing file: #{fm["image"]}" unless ROOT.join(fm["image"].delete_prefix("/")).exist?
  end

  if fm.key?("content_type") && !CONTENT_TYPES.include?(fm["content_type"])
    problems << "content_type '#{fm["content_type"]}' is not one of: #{CONTENT_TYPES.join(', ')}"
  elsif !fm.key?("content_type") && requires_content_type?(path)
    problems << "missing content_type (one of: #{CONTENT_TYPES.join(', ')})"
  end

  if requires_track_metadata?(path)
    problems << "missing track metadata key: track" unless fm.key?("track")
    if !fm.key?("pathways")
      problems << "missing track metadata key: pathways"
    elsif !fm["pathways"].is_a?(Array)
      problems << "pathways should be an Array"
    end
  end

  unless problems.empty?
    puts "[WARN] #{path} (#{t}): #{problems.join(' | ')}"
    PROBLEM_COUNT[:n] += 1
  end
end

PROBLEM_COUNT = { n: 0 }

puts "Running frontmatter validation from #{ROOT}..."

CONTENT_GLOBS.each do |pattern|
  Dir[ROOT.join(pattern)].sort.each do |file|
    validate_file(Pathname.new(file))
  end
end

if PROBLEM_COUNT[:n].zero?
  puts 'Validation complete: no problems found.'
  exit 0
end

puts "Validation complete: #{PROBLEM_COUNT[:n]} file(s) with problems."
exit 1
