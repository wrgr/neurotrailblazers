# frozen_string_literal: true
require 'yaml'
require 'cgi'

# Presentation supplements are intentionally separate from scored assessment data.
module DeckDesign
  ROOT = File.expand_path('../..', __dir__)
  DATA = YAML.safe_load(File.read(File.join(ROOT, '_data/module_deck_visuals.yml'), encoding: 'UTF-8'), aliases: false).fetch('modules')
  def self.e(value) = CGI.escapeHTML(value.to_s)

  def self.visual(item)
    content = case item.fetch('type')
    when 'figure'
      '<div class="visual-images">' + item.fetch('images').map do |im|
        src = '../../../../' + im.fetch('src').sub(%r{\A/}, '')
        "<figure><img src=\"#{e(src)}\" alt=\"#{e(im.fetch('alt'))}\"><figcaption>#{e(im.fetch('caption'))}</figcaption></figure>"
      end.join + '</div>'
    when 'flow'
      '<ol class="visual-steps">' + item.fetch('steps').each_with_index.map do |step, i|
        "<li><span class=\"step-number\" aria-hidden=\"true\">#{i + 1}</span><h3>#{e(step.fetch('label'))}</h3><p>#{e(step.fetch('text'))}</p></li>"
      end.join + '</ol>'
    when 'code'
      "<div class=\"visual-code\"><div><h3>Input and code</h3><pre><code>#{e(item.fetch('code'))}</code></pre></div><div><h3>Interpret the output</h3><pre class=\"output\">#{e(item.fetch('output'))}</pre></div></div>"
    when 'table'
      '<table><thead><tr>' + item.fetch('headers').map { |h| "<th scope=\"col\">#{e(h)}</th>" }.join + '</tr></thead><tbody>' +
        item.fetch('rows').map { |row| '<tr>' + row.each_with_index.map { |cell, j| j.zero? ? "<th scope=\"row\">#{e(cell)}</th>" : "<td>#{e(cell)}</td>" }.join + '</tr>' }.join + '</tbody></table>'
    when 'tree'
      # Native text and CSS topology, not a decorative image or an image answer key.
      '<div class="visual-tree"><p class="tree-root"><strong>A (0, 0)</strong><br>Root</p><p class="tree-stem">A–B: 3 µm</p><p class="tree-fork"><strong>B (0, 3)</strong><br>Branch point</p><div class="tree-children"><p><strong>C (−4, 3)</strong><br>B–C: 4 µm</p><p><strong>D (4, 3)</strong><br>B–D: 4 µm</p></div></div>'
    else
      raise "Unknown deck visual type: #{item['type']}"
    end
    <<~MD
      <!-- _class: visual-lesson -->
      ## #{item.fetch('title')}
      <p class="visual-lead">#{e(item.fetch('lead'))}</p>
      #{content}
      <p class="visual-question"><strong>Discuss:</strong> #{e(item.fetch('prompt'))}</p>
      <p class="source">#{e(item.fetch('source'))}</p>
      <!--
      Visual description and discussion guidance:
      #{item.fetch('description').gsub('-->', '-- >')}
      -->
    MD
  end

  # Keep the detailed source in presenter notes, split long lists rather than shrink.
  # Never rewrite an answer key or change a learning objective here.
  def self.chunk_slide(slide)
    return [slide] if slide.include?('_class:') || slide.include?('<div') || slide.include?('<table') || slide.include?('```')
    heading = slide[/\A\s*(## [^\n]+)/, 1]
    return [slide] unless heading
    notes = slide.scan(/<!--.*?-->/m).join("\n")
    body = slide.gsub(/<!--.*?-->/m, '').sub(/\A\s*## [^\n]+\n?/, '')
    lines = body.lines.map(&:rstrip).reject { |line| line.strip.empty? }
    return [slide] if lines.empty?
    added_notes = []
    lines = lines.map do |line|
      if line.start_with?('- ') && line.length > 260
        first = line.split(/(?<=[.!?])\s+(?=[A-Z])/).first
        if first.length.between?(40, 250)
          added_notes << line.sub(/\A- /, '')
          line = first
        end
      end
      line
    end
    pages = [[]]
    cost = ->(line) { (line.gsub(/<[^>]+>|\*\*|`/, '').length / 78.0).ceil + 0.5 }
    lines.each do |line|
      bullets = pages.last.count { |l| l.match?(/^\s*- /) }
      if pages.last.any? && ((line.match?(/^\s*- /) && bullets >= 4) || pages.last.sum { |l| cost.call(l) } + cost.call(line) > 10)
        pages << []
      end
      pages.last << line
    end
    extra = added_notes.empty? ? '' : "\n<!--\nFurther teaching detail from the module:\n#{added_notes.join("\n\n")}\n-->"
    pages.each_with_index.map do |page, i|
      name = i.zero? ? heading : heading.sub(/ \(continued\)\z/, '') + ' (continued)'
      "#{name}\n#{page.join("\n")}\n#{i.zero? ? notes + extra : ''}"
    end
  end

  def self.apply(path, num)
    text = File.read(path, encoding: 'UTF-8')
    front, body = text.match(/\A(---\n.*?\n---\n)(.*)\z/m).captures
    slides = body.split(/^---\s*$/).map(&:strip).reject(&:empty?)
    # These duplicated the capability and artifact slides without adding instruction.
    slides.reject! { |s| s.start_with?('## Session Outcomes') }
    slides = slides.flat_map { |s| chunk_slide(s) }
    visuals = DATA.fetch("module#{num}", []).map { |item| visual(item) }
    point = slides.index { |s| s.start_with?('## Studio Activity') } || slides.length - 1
    slides.insert(point, *visuals)
    # A reading route is available both on the slide and as a keyboard-focusable
    # control in the rendered presentation. The reader does not use SVG slides.
    slides << <<~MD
      <!-- _class: closing -->
      ## Read, review, or teach
      [Read these slides as a page](module#{num}.reader.html)

      [Open the complete lesson](https://www.neurotrailblazers.org/modules/module#{num}/)

      The reading version includes figure descriptions and discussion guidance.

      <p class="source">NeuroTrailblazers text: CC BY 4.0. Scientific figures retain their individual credits.</p>
    MD
    File.write(path, front + "\n" + slides.join("\n\n---\n\n") + "\n")
  end
end
