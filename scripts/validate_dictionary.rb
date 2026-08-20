#!/usr/bin/env ruby
# frozen_string_literal: true

# Hold _data/connectomics_dictionary.yml to the standard its own page states.
#
# technical-training/dictionary/index.md promises readers that entries carry a
# typical value where a term has a characteristic magnitude, a why-it-matters
# line where it drives a practical decision, and the confusion where one is
# routinely made -- then tells them to "treat the 'why it matters' line as the
# real content".
#
# In August 2026 that was true of a minority of entries: of 127 terms, 79 had
# `matters`, 27 had `typical`, 8 had `confuse`, and "Agglomeration" was five
# words with nothing else. A page that advertises a standard its data does not
# meet is the same defect class as the journal hub's "100+ papers", so it gets
# the same treatment: a gate.
#
# `typical` is conditional by design -- the page says "where a term has a
# characteristic magnitude". Terms that genuinely have none are listed below,
# so that omitting it stays a deliberate act rather than an oversight.

require "yaml"
require "pathname"

ROOT = Pathname.new(__dir__).parent
DATA = ROOT.join("_data/connectomics_dictionary.yml")

REQUIRED = %w[term category definition matters confuse units].freeze
MIN_DEFINITION_WORDS = 7

# Terms with no characteristic magnitude. Add to this deliberately, with a
# reason, rather than to silence the check.
NO_TYPICAL = {
  "Connectomics" => "names a field, not a measurable quantity",
}.freeze

problems = []

data = YAML.safe_load(DATA.read(encoding: "UTF-8"), aliases: true)
terms = data.is_a?(Hash) ? data.fetch("terms", []) : Array(data)

if terms.size < 120
  problems << "#{terms.size} terms; expected at least 120. If entries were removed " \
              "deliberately, move this floor."
end

seen = Hash.new(0)
terms.each do |t|
  name = t["term"].to_s
  label = name.empty? ? "(unnamed entry)" : name
  seen[name.downcase] += 1

  REQUIRED.each do |field|
    value = t[field]
    next unless value.nil? || (value.respond_to?(:empty?) && value.empty?)

    problems << "#{label}: missing #{field}"
  end

  definition = t["definition"].to_s
  if !definition.empty? && definition.split.size < MIN_DEFINITION_WORDS
    problems << "#{label}: definition is #{definition.split.size} words " \
                "(minimum #{MIN_DEFINITION_WORDS}). A label is not a definition."
  end

  if (t["typical"].nil? || t["typical"].to_s.empty?) && !NO_TYPICAL.key?(name)
    problems << "#{label}: no `typical`. Add one, or add the term to NO_TYPICAL " \
                "in this script with the reason it has no characteristic magnitude."
  end
end

duplicates = seen.select { |_, n| n > 1 }.keys.sort
unless duplicates.empty?
  problems << "duplicate term(s): #{duplicates.join(', ')}"
end

if problems.empty?
  with_typical = terms.count { |t| !t["typical"].to_s.empty? }
  puts "OK: #{terms.size} dictionary terms, all with definition/matters/confuse; " \
       "#{with_typical} with a typical value"
  exit 0
end

warn "Dictionary does not meet the standard its own page states:"
problems.first(40).each { |p| warn "  - #{p}" }
warn "  ... and #{problems.size - 40} more" if problems.size > 40
exit 1
