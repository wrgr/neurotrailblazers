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
  raw = File.read(path, encoding: 'UTF-8')
  parts = raw.split(/^---\s*$\n/, 3)
  return nil if parts.length < 3

  fm = YAML.safe_load(parts[1], permitted_classes: [Date], aliases: true) || {}
  body = parts[2]
  [fm, body]
end

# Matches a level-2 section by heading. Module pages vary their heading wording
# ("60-minute tutorial run-of-show" vs "Detailed run-of-show (90 minutes)",
# "Studio activity" vs "Studio activity: ..."), so fall back to a substring match
# before giving up. An exact match always wins.
def section(body, heading)
  exact = body.match(/^##\s+#{Regexp.escape(heading)}\s*$\n(.*?)(?=^##\s+|\z)/m)
  return exact[1].strip if exact

  key = heading.sub(/\A\d+-minute\s+/i, '').sub(/\Atutorial\s+/i, '')
  loose = body.match(/^##\s+[^\n]*#{Regexp.escape(key)}[^\n]*$\n(.*?)(?=^##\s+|\z)/mi)
  loose ? loose[1].strip : ''
end

def first_paragraph(text)
  text.split(/\n{2,}/).map(&:strip).find { |p| !p.empty? } || ''
end

def list_items(text)
  text.each_line.map(&:strip).select { |ln| ln.match?(/^(\-|\*|\d+\.)\s+/) }
end

# Collects misconception guardrail lines from a section. Skips headings, which may
# themselves contain the word (e.g. "### Misconception guardrails").
def misconception_items(text)
  text.each_line.map(&:strip).select do |ln|
    ln.downcase.include?('misconception') && !ln.start_with?('#')
  end
end

def normalize_bullets(items, fallback = '- See module page for details.')
  return fallback if items.empty?

  items.map { |i| i.sub(/^(\-|\*|\d+\.)\s+/, '- ') }.join("\n")
end

# Returns the body of a section with its sub-headings demoted one level, so a
# module section can be embedded under a worksheet heading without clashing.
def demote_headings(text)
  text.gsub(/^(#{'#'}{3,5})\s+/) { "#{Regexp.last_match(1)}# " }
end

# Pulls a labelled sub-block out of a section, e.g. the outputs list inside the
# Studio activity section. Module pages label these inconsistently, so accept all
# of: "**Outputs**", "**Outputs:**", "**Outputs**:", "### Outputs", "## Outputs".
# Returns '' when absent.
def labelled_block(text, label)
  lbl = Regexp.escape(label)
  patterns = [
    /^\*\*#{lbl}:?\*\*:?\s*$\n(.*?)(?=^\*\*|^\#{2,}\s|\z)/mi,
    /^\#{2,6}\s+#{lbl}\s*$\n(.*?)(?=^\#{2,6}\s|^\*\*|\z)/mi
  ]
  patterns.each do |rx|
    m = text.match(rx)
    return m[1].strip if m && !m[1].strip.empty?
  end
  ''
end

def inline_labelled(text, label)
  m = text.match(/^\*\*#{Regexp.escape(label)}:\*\*\s*(.+)$/)
  m ? m[1].strip : ''
end

# Extracts the "- **Technical:** ..." style rubric lines, keeping the label.
def rubric_lines(text)
  text.each_line.map(&:strip).select { |ln| ln.match?(/^\-\s+\*\*/) }
end

# Numbered steps, tolerating the bold-wrapped form some module pages use
# ("**1. 00:00-08:00 - Label**") as well as the plain "1. Label" form.
def numbered_steps(text)
  text.each_line.map(&:strip).select { |ln| ln.match?(/^(\*\*)?\d+\.\s+/) }
end

# Lines that begin with a time range, with or without bold or a leading number:
# "**00:00-08:00 | Label**", "1. **00:00-08:00** Label", "00:00-08:00 - Label".
def timed_lines(text)
  text.each_line.map(&:strip).select do |ln|
    ln.gsub('**', '').match?(/\A(\d+\.\s+)?\d{1,2}:\d{2}\s*[-\u2013\u2014]\s*\d{1,2}:\d{2}/)
  end
end

def bullet_or_dash(items, fallback)
  return fallback if items.empty?

  items.map { |i| i.sub(/^(\-|\*|\d+\.)\s+/, '') }
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
  concept_section = section(body, 'Concept set')
  workflow = first_paragraph(section(body, 'Core workflow'))
  workflow_section = section(body, 'Core workflow')
  run_of_show = section(body, 'run-of-show')
  activity_section = section(body, 'Studio activity')
  activity = first_paragraph(activity_section)
  rubric_section = section(body, 'Assessment rubric')
  rubric = first_paragraph(rubric_section)
  prompt = first_paragraph(section(body, 'Quick practice prompt'))
  references = Array(fm['references'])

  workflow_items = normalize_bullets(list_items(workflow_section))
  default_run = "- 00:00-08:00 frame the capability target and activate prior knowledge.\n" \
                "- 08:00-20:00 instructor models one worked example, thinking aloud about uncertainty.\n" \
                "- 20:00-38:00 guided learner activity.\n" \
                "- 38:00-50:00 debrief and misconception correction.\n" \
                "- 50:00-58:00 competency check.\n" \
                "- 58:00-60:00 exit prompt and next-step assignment."
  run_items = normalize_bullets(list_items(run_of_show), default_run)
  misconception_lines = normalize_bullets(misconception_items(concept_section), '- Surface and correct one likely misconception during debrief.')
  rubric_items = normalize_bullets(list_items(rubric_section), "- Use module rubric headings on the module page.")

  worksheet_mod_dir = File.join(WORKSHEET_DIR, "module#{num}")
  FileUtils.mkdir_p(worksheet_mod_dir)
  worksheet_path = File.join(worksheet_mod_dir, "module#{num}-activity.md")

  scenario = inline_labelled(activity_section, 'Scenario')
  scenario = activity if scenario.empty?
  outputs = bullet_or_dash(list_items(labelled_block(activity_section, 'Outputs')), [])
  outputs = bullet_or_dash(list_items(labelled_block(activity_section, 'Expected outputs')), []) if outputs.empty?
  task_steps = bullet_or_dash(numbered_steps(activity_section), [])
  task_steps = bullet_or_dash(numbered_steps(workflow_section), []) if task_steps.empty?
  workflow_steps = bullet_or_dash(numbered_steps(workflow_section), [])
  run_steps = bullet_or_dash(numbered_steps(run_of_show), [])
  run_steps = bullet_or_dash(timed_lines(run_of_show), []) if run_steps.empty?
  rubric_rows = rubric_lines(rubric_section)
  misconceptions = bullet_or_dash(misconception_items(concept_section), [])
  preclass = bullet_or_dash(list_items(section(body, 'Pre-class')), [])
  preclass = bullet_or_dash(list_items(labelled_block(run_of_show, 'Pre-class')), []) if preclass.empty?
  # Fall back to the free-text `prerequisites` field when the structured list is
  # empty. Modules 01-11 populate only the former, and reading just the list left
  # eleven worksheets showing a generic placeholder.
  prereqs = Array(fm['prerequisites_list'])
  if prereqs.empty? && !fm['prerequisites'].to_s.strip.empty?
    text = fm['prerequisites'].to_s.strip
    prereqs = text.casecmp('none').zero? ? [] : [text]
  end
  key_questions = Array(fm['key_questions'])
  duration = fm['duration'].to_s
  related_units = Array(fm['related_tools']) + Array(fm['datasets'])

  outputs_block =
    if outputs.empty?
      "- Artifact produced during the activity\n- One stated limitation or uncertainty\n- One revision made in response to feedback"
    else
      outputs.map { |o| "- #{o.sub(/,\z/, '').sub(/\.\z/, '')}" }.join("\n")
    end

  task_block =
    if task_steps.empty?
      "1. Read the scenario and restate the goal in your own words.\n2. Produce the artifact.\n3. Record evidence and limitations below."
    else
      task_steps.each_with_index.map { |t, k| "#{k + 1}. #{t}" }.join("\n")
    end

  workflow_block =
    if workflow_steps.empty?
      "- [ ] See the module page for the workflow."
    else
      workflow_steps.map { |w| "- [ ] #{w}" }.join("\n")
    end

  timing_block =
    if run_steps.empty?
      "| 00:00-08:00 | Frame the capability target |\n" \
      "| 08:00-20:00 | Model one worked example aloud |\n" \
      "| 20:00-38:00 | Guided learner activity |\n" \
      "| 38:00-50:00 | Debrief and misconception correction |\n" \
      "| 50:00-58:00 | Competency check |\n" \
      "| 58:00-60:00 | Exit prompt |"
    else
      run_steps.map do |r|
        clean = r.gsub('**', '').strip.sub(/\A\d+\.\s+/, '')
        time, _, rest = clean.partition(/\s*[|:\u2014-]\s+/)
        if rest.to_s.strip.empty? || !time.match?(/\d/)
          "| | #{clean.gsub('|', '/')} |"
        else
          "| #{time.strip} | #{rest.strip.gsub('|', '/')} |"
        end
      end.join("\n")
    end

  rubric_block =
    if rubric_rows.empty?
      "- Use the rubric headings on the module page."
    else
      rubric_rows.join("\n")
    end

  misconception_block =
    if misconceptions.empty?
      "- [ ] I have stated one thing I am still unsure about."
    else
      misconceptions.map do |m|
        text = m.gsub('**', '')
                .sub(/\A[-*\d.]+\s*/, '')
                .sub(/\AMisconception(\s+(guardrail|to\s+prevent|to\s+watch))?\s*:\s*/i, '')
                .strip
        text = text[0].upcase + text[1..].to_s unless text.empty?
        "- [ ] I did not assume: #{text}"
      end.join("\n")
    end

  prereq_block =
    if prereqs.empty? && fm['prerequisites'].to_s.strip.casecmp('none').zero?
      "- [ ] Nothing. This module assumes no prior work in this curriculum."
    elsif prereqs.empty?
      "- [ ] The module prerequisites listed on the module page"
    else
      prereqs.map { |p| "- [ ] #{p}" }.join("\n")
    end
  prereq_block += "\n" + preclass.map { |p| "- [ ] #{p}" }.join("\n") unless preclass.empty?

  question_block =
    if key_questions.empty?
      ''
    else
      "\n## Questions this module answers\n\nKeep these in view. At the end, answer each in one sentence.\n\n" +
        key_questions.each_with_index.map { |q, k| "#{k + 1}. #{q}\n   - Your answer:" }.join("\n") + "\n"
    end

  File.write(worksheet_path, <<~MD)
    # Module #{num} Activity Worksheet

    **Module:** #{title}#{duration.empty? ? '' : "  \n**Duration:** #{duration}"}  
    *Generated from the module page. Edit `modules/module#{num}.md`, not this file.*

    ---

    ## Capability target

    #{capability}

    You are done when you can demonstrate this, not when you have filled in every box below.

    ---

    ## Before you start

    Check that you have:

    #{prereq_block}

    Bring one question you already have about this topic. Write it here so you can check
    at the end whether it was answered:

    > My question:
    #{question_block}
    ---

    ## The task

    **Scenario:** #{scenario}

    #{task_block}

    ### What you hand in

    #{outputs_block}

    ---

    ## Working checklist

    Tick as you go. If you skip a step, write why — a skipped step with a stated reason
    is a decision; a skipped step without one is a gap.

    #{workflow_block}

    ---

    ## Evidence and reasoning

    Fill one row per claim you make in your artifact. A claim without a limitation is
    not finished.

    | # | Claim | Evidence (what specifically) | Limitation / what would change my mind |
    |---|---|---|---|
    | 1 | | | |
    | 2 | | | |
    | 3 | | | |

    **Confidence.** For your main claim, mark one and say why:

    - [ ] **High** — two or more independent lines of evidence agree
    - [ ] **Medium** — one strong line, or several that share a weakness
    - [ ] **Uncertain** — the deciding evidence is not available to me

    Why:

    **One alternative I considered and rejected**, and the reason:

    ---

    ## Misconception self-check

    These are the errors this module is designed to prevent. Confirm you did not make
    them, or note where you nearly did:

    #{misconception_block}

    ---

    ## Session timing (facilitator reference)

    | Time | Segment |
    |---|---|
    #{timing_block}

    ---

    ## Rubric

    Score yourself before anyone else does. Where you fall short, name the specific next
    action rather than a general intention.

    #{rubric_block}

    **My self-assessment:**

    - Strongest part of my work, and the evidence for that:
    - Weakest part, and the specific next action:

    ---

    ## Exit prompt

    #{prompt}

    **Your answer:**

    ---

    ## Peer review (swap worksheets)

    Reviewing someone else's reasoning is the fastest way to see the gaps in your own.
    Assess the **evidence quality**, not whether you agree with the conclusion.

    - Is every claim paired with specific evidence?
    - Is at least one limitation stated, and is it a real one?
    - Is the confidence level justified by the number of *independent* evidence lines?
    - One thing this person did better than me:
    - One question I would ask them:

    ---

    *Module page: `/modules/module#{num}/` · Slides: `/modules/slides/module#{num}/` · [Facilitator guide](/teaching/facilitator-guide/)*
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

    ## Session Outcomes
    - Learners can complete the module capability target.
    - Learners can produce one evidence-backed artifact.
    - Learners can state one limitation or uncertainty.

    ---

    ## Agenda (60 min)
    - 0-10 min: Frame and model
    - 10-35 min: Guided practice
    - 35-50 min: Debrief and misconception correction
    - 50-60 min: Competency check + exit ticket

    ---

    ## Capability Target
    #{capability}

    ---

    ## Concept Focus
    #{concept}

    ---

    ## Core Workflow
    #{workflow_items}

    ---

    ## 60-Minute Run-of-Show
    #{run_items}

    ---

    ## Misconceptions to Watch
    #{misconception_lines}

    ---

    ## Studio Activity
    #{activity}

    ---

    ## Activity Output Checklist
    - Evidence-linked artifact submitted.
    - At least one limitation or uncertainty stated.
    - Revision point captured from feedback.

    ---

    ## Assessment Rubric
    #{rubric_items}

    ---

    ## Exit Ticket
    #{prompt}

    ---

    ## References (Instructor)
    #{references.empty? ? "- Use module references listed on the module page." : references.map { |r| "- #{r}" }.join("\n")}

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

    <div class="resource-card">
      <p>This page provides the teaching slide artifacts and related delivery materials.</p>
      <div class="resource-links">
        <a class="resource-link" href="{{ '/course/decks/marp/out/modules/module#{num}.html' | relative_url }}">Open HTML Deck</a>
        <a class="resource-link" href="{{ '/course/decks/marp/out/modules/module#{num}.pptx' | relative_url }}">Download PowerPoint (.pptx)</a>
        <a class="resource-link" href="{{ '/assets/worksheets/module#{num}/module#{num}-activity.md' | relative_url }}">Open Worksheet</a>
        <a class="resource-link" href="{{ '/modules/module#{num}/' | relative_url }}">Open Module Page</a>
      </div>
      <p><strong>Slide source path:</strong> <code>course/decks/marp/modules/module#{num}.marp.md</code></p>
    </div>
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

  <p>Need full lesson kits and facilitator guidance? Visit the <a href="{{ '/teaching/' | relative_url }}">Teaching Hub</a>.</p>

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
