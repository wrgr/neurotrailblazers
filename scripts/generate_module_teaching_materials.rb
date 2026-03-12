#!/usr/bin/env ruby
# frozen_string_literal: true

require 'yaml'
require 'fileutils'
require 'date'

ROOT = File.expand_path('..', __dir__)
MODULE_DIR = File.join(ROOT, 'modules')
SLIDE_PAGE_DIR = File.join(ROOT, 'modules', 'slides')
MARP_DIR = File.join(ROOT, 'course', 'decks', 'marp', 'modules')
WORKSHEET_DIR = File.join(ROOT, 'assets', 'worksheets')

def parse_file(path)
  raw = File.read(path)
  parts = raw.split(/^---\s*$\n/, 3)
  return nil if parts.length < 3

  fm = YAML.safe_load(parts[1], permitted_classes: [Date], aliases: true) || {}
  body = parts[2]
  [fm, body]
end

def section(body, heading)
  rx = /^##\s+#{Regexp.escape(heading)}\s*$\n(.*?)(?=^##\s+|\z)/m
  match = body.match(rx)
  match ? match[1].strip : ''
end

def first_paragraph(text)
  text.split(/\n{2,}/).map(&:strip).find { |p| !p.empty? } || ''
end

FileUtils.mkdir_p(SLIDE_PAGE_DIR)
FileUtils.mkdir_p(MARP_DIR)
FileUtils.mkdir_p(WORKSHEET_DIR)

module_paths = Dir.glob(File.join(MODULE_DIR, 'module*.md')).sort
count = 0

module_paths.each do |path|
  parsed = parse_file(path)
  next unless parsed

  fm, body = parsed
  number = fm['module_number'].to_i
  slug = fm['slug'].to_s
  title = fm['title'].to_s
  objectives = Array(fm['learning_objectives'])
  num = format('%02d', number)

  capability = first_paragraph(section(body, 'Capability target'))
  concept = first_paragraph(section(body, 'Concept set'))
  workflow = first_paragraph(section(body, 'Core workflow'))
  run_of_show = section(body, '60-minute tutorial run-of-show')
  activity = first_paragraph(section(body, 'Studio activity'))
  rubric = first_paragraph(section(body, 'Assessment rubric'))
  prompt = first_paragraph(section(body, 'Quick practice prompt'))

  worksheet_mod_dir = File.join(WORKSHEET_DIR, "module#{num}")
  FileUtils.mkdir_p(worksheet_mod_dir)
  worksheet_path = File.join(worksheet_mod_dir, "module#{num}-activity.md")
  File.write(worksheet_path, <<~MD)
    # Module #{num} Activity Worksheet

    ## Module
    #{title}

    ## Capability Target
    #{capability}

    ## Studio Activity Instructions
    #{activity}

    ## Evidence and Reasoning Notes
    - Claim:
    - Evidence:
    - Limitation:

    ## Rubric Check
    #{rubric}

    ## Exit Prompt
    #{prompt}
  MD

  marp_path = File.join(MARP_DIR, "module#{num}.marp.md")
  File.write(marp_path, <<~MD)
    ---
    marp: true
    theme: default
    paginate: true
    title: "#{title}"
    ---

    # #{title}
    Teaching Deck

    ---

    ## Learning Objectives
    #{objectives.map { |o| "- #{o}" }.join("\n")}

    ---

    ## Capability Target
    #{capability}

    ---

    ## Concept Focus
    #{concept}

    ---

    ## Core Workflow
    #{workflow}

    ---

    ## 60-Minute Run-of-Show
    #{run_of_show.empty? ? "- See module page for timed delivery flow." : run_of_show}

    ---

    ## Studio Activity
    #{activity}

    ---

    ## Assessment Rubric
    #{rubric}

    ---

    ## Quick Practice Prompt
    #{prompt}

    ---

    ## Teaching Materials
    - Module page: /modules/module#{num}/
    - Slide page: /modules/slides/module#{num}/
    - Worksheet: /assets/worksheets/module#{num}/module#{num}-activity.md
  MD

  slide_page_path = File.join(SLIDE_PAGE_DIR, "module#{num}.md")
  File.write(slide_page_path, <<~MD)
    ---
    layout: page
    title: "Slide Deck: Module #{num}"
    permalink: /modules/slides/module#{num}/
    slug: module#{num}-slides
    track: core-concepts-methods
    pathways:
      - classroom delivery
      - teaching preparation
    ---

    ## Slide Deck for #{title}

    This page provides the teaching slide source and related delivery materials.

    - Slide source (`marp`): `/course/decks/marp/modules/module#{num}.marp.md`
    - Activity worksheet: `/assets/worksheets/module#{num}/module#{num}-activity.md`
    - Module page: [#{title}]({{ '/modules/module#{num}/' | relative_url }})
  MD

  count += 1
end

index_path = File.join(SLIDE_PAGE_DIR, 'index.md')
File.write(index_path, <<~MD)
  ---
  layout: page
  title: "Module Slide Decks"
  permalink: /modules/slides/
  slug: module-slides
  track: core-concepts-methods
  pathways:
    - classroom delivery
  ---

  ## Module Slide Decks

  <div class="cards-grid">
  {% assign module_pages = site.pages | where_exp: 'p', \"p.path contains 'modules/slides/module'\" | sort: 'path' %}
  {% for p in module_pages %}
    <article class="card">
      <h3 class="card-title"><a href="{{ p.url | relative_url }}">{{ p.title }}</a></h3>
      <p class="card-description">Slide source and worksheet links for instructional delivery.</p>
    </article>
  {% endfor %}
  </div>
MD

puts "Generated teaching materials for #{count} modules."
