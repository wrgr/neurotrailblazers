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
  "models.md",
  "education/models.md",
].freeze

REQUIRED_BY_TYPE = {
  "modules" => %w[title module_number slug short_title pipeline_stage status],
  "avatars" => %w[layout title role permalink slug summary strengths challenges goals recommended_modules recommended_datasets recommended_tools image last_reviewed maintainer],
  "datasets" => %w[layout title slug summary modality species scale access_level use_cases recommended_modules related_tools related_frameworks resource_links image last_reviewed maintainer],
  "tools" => %w[layout title slug summary use_cases recommended_modules related_datasets last_reviewed maintainer],
  "frameworks" => %w[layout title slug summary framework_type related_modules related_tools last_reviewed maintainer],
}.freeze

MODULE_ASSET_FIELDS = %w[slides notebook downloads].freeze

def extract_frontmatter(path)
  text = path.read
  return nil unless text.start_with?("---")

  parts = text.split(/^---\s*$\n?/)
  # parts: ["", "yaml", "content..."] or similar
  yaml = parts[1]
  YAML.safe_load(yaml, [Date]) || {}
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

  unless problems.empty?
    puts "[WARN] #{path} (#{t}): #{problems.join(' | ')}"
  end
end

puts "Running frontmatter validation from #{ROOT}..."

CONTENT_GLOBS.each do |pattern|
  Dir[ROOT.join(pattern)].sort.each do |file|
    validate_file(Pathname.new(file))
  end
end

puts "Validation complete."
