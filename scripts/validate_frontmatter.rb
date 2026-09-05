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

# ---------------------------------------------------------------------------
# Track catalogue reconciliation.
#
# Three sources used to disagree about how long a track takes: the module pages'
# `duration:` front matter, the hours budgeted per sequence step in
# `_data/track_catalog.yml`, and each track's prose `time_estimate`. The
# convention now (documented at the top of track_catalog.yml) is that every
# `hours:` figure is TOTAL LEARNER HOURS, the same quantity module pages declare.
# A step covering curriculum modules names them in `modules:` and carries a
# `module_hours:` equal to the sum of those modules' declared duration midpoints.
#
# The gates below make drift a build failure rather than a reading exercise.

# "3-4 hours" -> 3.5, "4 hours" -> 4.0, "4-6 hours" -> 5.0
def duration_midpoint(raw)
  return nil unless raw.is_a?(String)

  m = raw.match(/(\d+(?:\.\d+)?)\s*(?:-|\u2013)\s*(\d+(?:\.\d+)?)/)
  return (m[1].to_f + m[2].to_f) / 2.0 if m

  m = raw.match(/(\d+(?:\.\d+)?)/)
  m ? m[1].to_f : nil
end

# Module numbers named in a step's rendered `do:` prose. Deliberately keyed on
# the word "Module"/"Modules" so "Technical Unit 08" is never mistaken for one.
def modules_in_prose(text)
  nums = []
  pattern = /\bModules?\s+((?:\d{1,2}(?:\s*[-\u2013]\s*\d{1,2})?)(?:\s*(?:,|and)\s*\d{1,2}(?:\s*[-\u2013]\s*\d{1,2})?)*)/
  text.to_s.scan(pattern) do |match|
    match[0].split(/\s*(?:,|and)\s*/).each do |tok|
      tok = tok.strip
      if (r = tok.match(/\A(\d{1,2})\s*[-\u2013]\s*(\d{1,2})\z/))
        nums.concat((r[1].to_i..r[2].to_i).to_a)
      elsif (r = tok.match(/\A(\d{1,2})\z/))
        nums << r[1].to_i
      end
    end
  end
  nums.uniq.sort
end

def module_durations
  @module_durations ||= begin
    out = {}
    Dir[ROOT.join("modules/module*.md")].sort.each do |file|
      path = Pathname.new(file)
      fm = extract_frontmatter(path)
      next if fm.nil?

      num = fm["module_number"]
      next unless num.is_a?(Integer)

      hours = duration_midpoint(fm["duration"])
      if hours.nil?
        puts "[WARN] #{path}: duration front matter is missing or unparseable (#{fm["duration"].inspect})"
        PROBLEM_COUNT[:n] += 1
        next
      end
      out[num] = hours
    end
    out
  end
end

def fmt_hours(value)
  value == value.round ? value.round.to_s : format("%.1f", value)
end

def validate_track_catalog
  catalog_path = ROOT.join("_data", "track_catalog.yml")
  return unless catalog_path.exist?

  catalog = YAML.safe_load(catalog_path.read(encoding: "UTF-8"), permitted_classes: [Date], aliases: true) || {}
  durations = module_durations

  Array(catalog["tracks"]).each do |track|
    slug = track["slug"] || "(unnamed track)"
    problems = []

    declared = Array(track["module_numbers"])
    steps = Array(track["sequence"])

    sequenced = []
    step_hours_total = 0.0
    module_hours_total = 0.0

    steps.each_with_index do |step, idx|
      label = "step #{idx + 1} (#{step["step"]})"
      hours = step["hours"]
      if hours.is_a?(Numeric)
        step_hours_total += hours.to_f
      else
        problems << "#{label}: missing numeric hours"
      end

      prose = modules_in_prose(step["do"])
      listed = Array(step["modules"]).select { |n| n.is_a?(Integer) }

      if step.key?("modules") && Array(step["modules"]).size != listed.size
        problems << "#{label}: modules: must be a list of integers"
      end

      # The prose is what a learner reads; the list is what the site can check.
      if listed.sort != prose
        problems << "#{label}: prose names modules #{prose.inspect} but modules: says #{listed.sort.inspect}"
      end

      next if listed.empty?

      repeated = listed & sequenced
      problems << "#{label}: modules #{repeated.inspect} already covered by an earlier step (module_hours would double-count)" unless repeated.empty?
      sequenced.concat(listed)

      missing_pages = listed.reject { |n| durations.key?(n) }
      problems << "#{label}: no module page for #{missing_pages.inspect}" unless missing_pages.empty?

      expected = listed.select { |n| durations.key?(n) }.sum { |n| durations[n] }
      module_hours_total += expected

      unless step.key?("module_hours")
        problems << "#{label}: covers modules but declares no module_hours (expected #{fmt_hours(expected)})"
        next
      end

      declared_mh = step["module_hours"]
      unless declared_mh.is_a?(Numeric)
        problems << "#{label}: module_hours must be numeric"
        next
      end

      if (declared_mh.to_f - expected).abs > 0.05
        problems << "#{label}: module_hours #{fmt_hours(declared_mh.to_f)} but the module pages declare #{fmt_hours(expected)}"
      end

      if hours.is_a?(Numeric) && hours.to_f + 0.05 < declared_mh.to_f
        problems << "#{label}: hours #{fmt_hours(hours.to_f)} is less than its own module_hours #{fmt_hours(declared_mh.to_f)}"
      end
    end

    steps.each_with_index do |step, idx|
      next unless step.key?("module_hours")
      next unless Array(step["modules"]).empty?

      problems << "step #{idx + 1} (#{step["step"]}): declares module_hours without modules:"
    end

    unsequenced = declared - sequenced
    problems << "module_numbers #{unsequenced.inspect} appear on the track card but in no sequence step" unless unsequenced.empty?

    unlisted = sequenced.uniq - declared
    problems << "sequence steps cover modules #{unlisted.inspect} that are not in module_numbers" unless unlisted.empty?

    declared_module_hours = declared.select { |n| durations.key?(n) }.sum { |n| durations[n] }
    if (module_hours_total - declared_module_hours).abs > 0.05 && unsequenced.empty? && unlisted.empty?
      problems << "sequence module hours total #{fmt_hours(module_hours_total)} but module_numbers declare #{fmt_hours(declared_module_hours)}"
    end

    estimate = track["time_estimate"].to_s
    if (m = estimate.match(/(\d+(?:\.\d+)?)\s*(?:-|\u2013)\s*(\d+(?:\.\d+)?)\s*hours/))
      low = m[1].to_f
      high = m[2].to_f
      if step_hours_total < low || step_hours_total > high
        problems << "sequence step hours total #{fmt_hours(step_hours_total)} falls outside time_estimate \"#{estimate}\""
      end
    else
      problems << "time_estimate does not state an N-M hours range: #{estimate.inspect}"
    end

    next if problems.empty?

    puts "[WARN] _data/track_catalog.yml (#{slug}): #{problems.join(' | ')}"
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

validate_track_catalog

if PROBLEM_COUNT[:n].zero?
  puts 'Validation complete: no problems found.'
  exit 0
end

puts "Validation complete: #{PROBLEM_COUNT[:n]} file(s) with problems."
exit 1
