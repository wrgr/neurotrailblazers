#!/usr/bin/env ruby
# frozen_string_literal: true

# Fail the build when JavaScript toggles a class onto an element that no CSS rule
# can match.
#
# Two live defects motivated this, both shipped and both invisible to every
# existing gate, because every validator in CI reads text and none of them has
# ever asked whether a style actually applies:
#
#   1. technical-training/journal-club/index.md marked four elements
#      class="... hidden" and toggled `hidden` from JS. The only rule in the whole
#      stylesheet was `.jc-card.hidden`, which cannot match `.jc-prompt-modal`, so
#      the full-viewport AI-synthesis modal (position:fixed, inset:0, z-index:1000)
#      painted on page load and swallowed every click on the site nav. Its close
#      button added a class nothing listened to. The page was unusable.
#   2. technical-training/dictionary/index.md toggles `is-active` on its eight
#      category buttons and no rule for it existed anywhere, so the 127-term
#      dictionary filtered correctly and never said what it had filtered to.
#
# Both are the same failure: a class the script depends on that the stylesheet
# never defines *for that element*. Note the qualifier -- a check for "does the
# name `hidden` appear in the CSS at all" passes defect 1, because `.jc-card.hidden`
# contains it. So the rule here is specificity-aware:
#
#   For each element carrying a JS-toggled class C in its markup, at least one CSS
#   compound selector mentioning C must have all of its classes present on that
#   element. `.hidden` and `div.hidden` satisfy any element; `.jc-card.hidden`
#   satisfies only elements that also carry `jc-card`.
#
# A class that appears in no static markup (JS builds the element, or adds the
# class to something it found by id) has nothing to check specificity against, and
# falls back to the weaker question: does any rule mention it at all? That is all
# that can be known without running the page.
#
# Rules are read from the shared stylesheets *and* from every <style> block on the
# page itself, since several pages style their own widgets inline.
#
# What this does NOT do, and the reason the stronger item stays open in
# NEXT_CONTENT_PASS.md: nothing here loads a page, clicks the controls and asserts
# the nav is still reachable. This is a static approximation of that smoke test.

require 'set'

ROOT = File.expand_path('..', __dir__)

# course/decks/marp/out/ is Marp's own generated output: its classes come from a
# bundled theme inlined at render time, not from this site's stylesheet.
SKIP_PREFIXES = %w[
  vendor/ _site/ node_modules/ .git/ .chrome course/decks/marp/out/
].freeze

SOURCE_GLOBS = ['**/*.md', '**/*.html', 'assets/js/**/*.js'].freeze

GLOBAL_CSS = [
  'assets/css/site-styles.css',
  'assets/brand/brand-tokens.css'
].freeze

# Classes that are documented examples rather than live behaviour: the planning
# notes quote the defects above verbatim while describing them.
SKIP_FILES = %w[docs/].freeze

# Toggled via classList.add / .remove / .toggle / .replace. `.contains` is a read,
# and anything it reads had to be added by one of the above to matter.
#
# The method name is captured because the arguments are not uniform:
# add/remove/replace take class names in every position, but
# `toggle(cls, force)` takes a *condition* second. Reading that condition as a
# class name is not theoretical -- `toggle('active', b.dataset.mode === 'organic')`
# and `toggle('active', type === 'citation')` both appear on this site, and an
# extractor that takes every string literal invents `organic`, `citation` and
# `coauthor` as classes that must be styled.
TOGGLE_CALL = /classList\s*\.\s*(add|remove|toggle|replace)\s*\(([^)]*)\)/m.freeze
QUOTED = /'([^']*)'|"([^"]*)"|`([^`\\$]*)`/.freeze

CLASS_ATTR = /class\s*=\s*(?:"([^"]*)"|'([^']*)')/m.freeze
STYLE_BLOCK = %r{<style[^>]*>(.*?)</style>}m.freeze

# A class name that is built at runtime -- `'tier-' + n` -- reaches us as a
# fragment. Nothing static can check those.
VALID_CLASS = /\A-?[A-Za-z_][\w-]*\z/.freeze

def source_files
  SOURCE_GLOBS.flat_map { |g| Dir.glob(File.join(ROOT, g)) }.reject do |path|
    rel = path.sub("#{ROOT}/", '')
    SKIP_PREFIXES.any? { |p| rel.start_with?(p) } ||
      SKIP_FILES.any? { |p| rel.start_with?(p) }
  end.sort.uniq
end

# Every compound selector in a stylesheet, as a set of the class names it requires.
# `.a .b > .c.d` yields {a}, {b} and {c,d}: an element matches the last compound
# only if it carries both c and d.
#
# Hand-rolled rather than regexed in one pass because brace depth matters --
# selectors inside @media must be collected, declarations inside @font-face must
# not be mistaken for them (they parse to compounds with no classes, and are
# dropped).
def compounds(css)
  css = css.gsub(%r{/\*.*?\*/}m, ' ')
  out = []
  buf = +''
  depth = 0
  css.each_char do |ch|
    case ch
    when '{'
      sel = buf.strip
      out.concat(split_compounds(sel)) unless sel.empty? || sel.start_with?('@')
      buf = +''
      depth += 1
    when '}'
      depth -= 1
      buf = +''
    when ';'
      buf = +''
    else
      buf << ch
    end
  end
  out
end

def split_compounds(selector_list)
  selector_list.split(',').flat_map do |selector|
    # Split on descendant, child, adjacent and general-sibling combinators.
    # No filter_map (2.7+): CI runs these scripts on 3.3, but the Ruby on this
    # project's own machines is 2.6, and two sibling validators already cannot be
    # run locally for exactly this reason. Staying inside 2.6 costs nothing here
    # and keeps the gate runnable before a push.
    selector.split(/[\s>+~]+/).map do |compound|
      # Drop pseudo-elements and functional pseudo-classes' arguments, so
      # `.a:not(.b)` requires only `a` -- the safe direction, since treating a
      # negation as a requirement would invent failures.
      bare = compound.gsub(/:{1,2}[\w-]+(\([^)]*\))?/, '')
      names = bare.scan(/\.([\w-]+)/).flatten
      names.empty? ? nil : Set.new(names)
    end.compact
  end
end

# The class names JS hands to classList, and the file offset of each call, so a
# finding can name a line.
def toggled_classes(text)
  found = Hash.new { |h, k| h[k] = [] }
  text.to_enum(:scan, TOGGLE_CALL).each do
    m = Regexp.last_match
    method = m[1]
    line = text[0, m.begin(0)].count("\n") + 1

    literals = []
    m[2].scan(QUOTED) do
      lm = Regexp.last_match
      literals << (lm[1] || lm[2] || lm[3])
    end
    # toggle's second argument is the force condition, not a class.
    literals = literals.first(1) if method == 'toggle'

    literals.each do |literal|
      next if literal.nil? || literal.empty?

      # `classList.add('a', 'b')` and `add('a b')` are both legal.
      literal.split(/\s+/).each do |name|
        found[name] << line if VALID_CLASS.match?(name)
      end
    end
  end
  found
end

# Every class="..." on the page, including those inside JS template strings that
# build markup -- the same regex finds both, which is what we want.
def element_class_sets(text)
  text.scan(CLASS_ATTR).map do |dq, sq|
    raw = dq || sq
    # Liquid output and tags are not class names.
    raw = raw.gsub(/\{\{.*?\}\}/m, ' ').gsub(/\{%.*?%\}/m, ' ')
    Set.new(raw.split(/\s+/).select { |c| VALID_CLASS.match?(c) })
  end
end

def satisfied?(klass, element_classes, rules)
  mentioning = rules.select { |compound| compound.include?(klass) }
  return false if mentioning.empty?

  mentioning.any? { |compound| compound.subset?(element_classes) }
end

def main
  puts "Running JS-toggled class validation from #{ROOT}..."

  global_css = GLOBAL_CSS.map { |f| File.read(File.join(ROOT, f), encoding: 'UTF-8') }.join("\n")
  global_rules = compounds(global_css)

  problems = []

  source_files.each do |path|
    rel = path.sub("#{ROOT}/", '')
    text = File.read(path, encoding: 'UTF-8')
    next unless text.include?('classList')

    toggles = toggled_classes(text)
    next if toggles.empty?

    local_rules = text.scan(STYLE_BLOCK).flatten.flat_map { |css| compounds(css) }
    rules = global_rules + local_rules

    elements = element_class_sets(text)

    toggles.each do |klass, lines|
      carriers = elements.select { |s| s.include?(klass) }

      if carriers.empty?
        # No element on the page declares the class, so there is nothing to check
        # specificity against -- JS builds the element, or reaches it by id. The
        # weaker question is all that is answerable: does any rule mention it?
        #
        # Deliberately not "does an *unqualified* rule mention it". The honest
        # pattern on this site is a qualified pair -- `.nn-opt-btn.correct`,
        # `.reveal.is-visible`, `.nt-hotspot.is-selected` -- applied to an element
        # that plainly carries the base class, and demanding an unqualified rule
        # would fail all three while catching nothing. Both real defects are still
        # caught: `is-active` was mentioned by no rule at all, and `hidden` had
        # carriers, so it took the precise branch above.
        next if rules.any? { |compound| compound.include?(klass) }

        problems << [rel, lines.first,
                     "JS toggles `#{klass}` but no CSS rule anywhere mentions it " \
                     '(no element on the page declares it either)']
      else
        unmatched = carriers.reject { |s| satisfied?(klass, s, rules) }
        next if unmatched.empty?

        example = unmatched.first.to_a.sort.join(' ')
        problems << [rel, lines.first,
                     "JS toggles `#{klass}` on an element that no rule for it can match " \
                     "(element carries: #{example})"]
      end
    end
  end

  if problems.empty?
    puts 'Validation complete: no problems found.'
    return 0
  end

  problems.sort.each { |rel, line, msg| puts "[FAIL] #{rel}:#{line}: #{msg}" }
  puts
  puts "#{problems.size} problem(s) found."
  1
end

exit(main) if $PROGRAM_NAME == __FILE__
