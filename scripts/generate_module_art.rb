#!/usr/bin/env ruby
# Generates the module artwork: one deterministic SVG banner per module in
# assets/images/modules/moduleNN.svg. Vector art, not photographs: every image
# is generated from this script, so there is nothing to license and nothing to
# drift. The visual system is shared -- a deep neuropil ground with a faint
# node-and-edge web, tinted by the module's pipeline stage -- and the central
# motif is specific to each module's topic.
#
# Deterministic: same script, same output (seeded per module number).
# Regenerate with:  ruby scripts/generate_module_art.rb
# Do not hand-edit the SVGs; edit the motif here and re-run.

require "yaml"
require "date"
require "pathname"

ROOT = Pathname.new(__dir__).parent
OUT_DIR = ROOT.join("assets/images/modules")

W = 1200
H = 420
CX = W / 2.0
CY = H / 2.0

# Stage accents match the module-card accents in site-styles.css.
STAGE_ACCENT = {
  "Foundations" => "#2563eb",   # --neural-blue
  "Question" => "#f59e0b",
  "Experiment" => "#10b981",
  "Analysis" => "#f97316",
  "Dissemination" => "#7c3aed", # --cerebral-purple
}.freeze

INK = "#e2e8f0"        # light strokes on the dark ground
GROUND_A = "#0f172a"
GROUND_B = "#111c33"
CYAN = "#06b6d4"       # --axon-cyan, shared secondary across all stages

class Svg
  attr_reader :parts

  def initialize
    @parts = []
  end

  def <<(fragment)
    @parts << fragment
    self
  end

  def circle(x, y, r, fill: "none", stroke: "none", sw: 0, opacity: nil, dash: nil)
    self << %(<circle cx="#{f x}" cy="#{f y}" r="#{f r}" fill="#{fill}" stroke="#{stroke}" stroke-width="#{f sw}"#{op opacity}#{da dash}/>)
  end

  def line(x1, y1, x2, y2, stroke:, sw:, opacity: nil, dash: nil, cap: "round")
    self << %(<line x1="#{f x1}" y1="#{f y1}" x2="#{f x2}" y2="#{f y2}" stroke="#{stroke}" stroke-width="#{f sw}" stroke-linecap="#{cap}"#{op opacity}#{da dash}/>)
  end

  def rect(x, y, w, h, rx: 0, fill: "none", stroke: "none", sw: 0, opacity: nil)
    self << %(<rect x="#{f x}" y="#{f y}" width="#{f w}" height="#{f h}" rx="#{f rx}" fill="#{fill}" stroke="#{stroke}" stroke-width="#{f sw}"#{op opacity}/>)
  end

  def path(d, fill: "none", stroke: "none", sw: 0, opacity: nil, dash: nil, cap: "round")
    self << %(<path d="#{d}" fill="#{fill}" stroke="#{stroke}" stroke-width="#{f sw}" stroke-linecap="#{cap}" stroke-linejoin="round"#{op opacity}#{da dash}/>)
  end

  def poly(points, fill: "none", stroke: "none", sw: 0, opacity: nil)
    pts = points.map { |(x, y)| "#{f x},#{f y}" }.join(" ")
    self << %(<polygon points="#{pts}" fill="#{fill}" stroke="#{stroke}" stroke-width="#{f sw}"#{op opacity}/>)
  end

  def to_s
    @parts.join("\n")
  end

  private

  def f(v)
    v.is_a?(Float) ? v.round(2) : v
  end

  def op(opacity)
    opacity ? %( opacity="#{opacity}") : ""
  end

  def da(dash)
    dash ? %( stroke-dasharray="#{dash}") : ""
  end
end

# --- shared ground -----------------------------------------------------------

def defs(accent)
  <<~SVG
    <defs>
      <linearGradient id="ground" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0" stop-color="#{GROUND_A}"/>
        <stop offset="1" stop-color="#{GROUND_B}"/>
      </linearGradient>
      <radialGradient id="mist" cx="0.5" cy="0.5" r="0.5">
        <stop offset="0" stop-color="#{accent}" stop-opacity="0.22"/>
        <stop offset="1" stop-color="#{accent}" stop-opacity="0"/>
      </radialGradient>
      <radialGradient id="mist2" cx="0.5" cy="0.5" r="0.5">
        <stop offset="0" stop-color="#{CYAN}" stop-opacity="0.14"/>
        <stop offset="1" stop-color="#{CYAN}" stop-opacity="0"/>
      </radialGradient>
    </defs>
  SVG
end

def mist_blob(svg, rng, which, count)
  count.times do
    r = 120 + rng.rand(190)
    x = rng.rand(W)
    y = rng.rand(H)
    svg << %(<circle cx="#{x}" cy="#{y}" r="#{r}" fill="url(##{which})"/>)
  end
end

# A faint field of connected nodes: the neuropil every module sits inside.
def web(svg, rng, accent)
  nodes = Array.new(16) { [rng.rand(W), rng.rand(H)] }
  nodes.combination(2) do |(a, b)|
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    dist = Math.sqrt(dx * dx + dy * dy)
    next if dist > 260

    svg.line(a[0], a[1], b[0], b[1], stroke: INK, sw: 1, opacity: 0.07)
  end
  nodes.each do |(x, y)|
    svg.circle(x, y, 2.2 + rng.rand * 1.6, fill: accent, opacity: 0.28)
  end
end

def ground(svg, rng, accent)
  svg.rect(0, 0, W, H, fill: "url(#ground)")
  mist_blob(svg, rng, "mist", 3)
  mist_blob(svg, rng, "mist2", 2)
  web(svg, rng, accent)
end

# --- small shared figures ----------------------------------------------------

def soma(svg, x, y, r, accent, opacity: 1)
  svg.circle(x, y, r, fill: accent, opacity: 0.18 * opacity)
  svg.circle(x, y, r, stroke: accent, sw: 3, opacity: 0.9 * opacity)
  svg.circle(x, y, r * 0.42, fill: INK, opacity: 0.55 * opacity)
end

def arrow(svg, x1, y1, x2, y2, color, sw: 3, opacity: 0.9)
  svg.line(x1, y1, x2, y2, stroke: color, sw: sw, opacity: opacity)
  ang = Math.atan2(y2 - y1, x2 - x1)
  [ang + 2.6, ang - 2.6].each do |a|
    svg.line(x2, y2, x2 + 14 * Math.cos(a), y2 + 14 * Math.sin(a), stroke: color, sw: sw, opacity: opacity)
  end
end

# Recursive dendritic branch.
def branch(svg, rng, x, y, angle, length, depth, accent)
  return if depth.zero? || length < 12

  x2 = x + length * Math.cos(angle)
  y2 = y + length * Math.sin(angle)
  svg.line(x, y, x2, y2, stroke: accent, sw: [depth, 5].min, opacity: 0.85)
  svg.circle(x2, y2, 2.4, fill: INK, opacity: 0.6) if depth <= 2
  kids = depth > 3 ? 2 : (rng.rand < 0.75 ? 2 : 1)
  kids.times do
    spread = 0.32 + rng.rand * 0.5
    sign = rng.rand < 0.5 ? -1 : 1
    branch(svg, rng, x2, y2, angle + sign * spread + (rng.rand - 0.5) * 0.2,
           length * (0.66 + rng.rand * 0.14), depth - 1, accent)
  end
end

# --- per-module motifs -------------------------------------------------------
# Each takes (svg, rng, accent) and draws the central figure.

MOTIFS = {}

# 01 Scientific Curiosity & Motivation: a question-mark of nodes resolving into a testable path.
MOTIFS[1] = lambda do |svg, rng, accent|
  pts = []
  # Question-mark curve traced by nodes.
  20.times do |i|
    t = i / 19.0
    a = Math::PI * 1.35 * t - Math::PI * 0.95
    r = 96 - 26 * t
    pts << [CX - 60 + r * Math.cos(a), CY - 44 + r * Math.sin(a)] if t < 0.72
  end
  pts << [CX - 60, CY + 52]
  pts.each_cons(2) { |a, b| svg.line(a[0], a[1], b[0], b[1], stroke: accent, sw: 5, opacity: 0.9) }
  pts.each { |(x, y)| svg.circle(x, y, 5, fill: INK, opacity: 0.85) }
  svg.circle(CX - 60, CY + 96, 8, fill: accent)
  # The question resolving into a measured path with milestones.
  arrow(svg, CX - 20, CY + 96, CX + 250, CY + 96, INK, sw: 3, opacity: 0.7)
  [70, 140, 210].each { |dx| svg.circle(CX - 20 + dx, CY + 96, 6, stroke: accent, sw: 3) }
  soma(svg, CX + 170, CY - 60, 40, accent)
  branch(svg, rng, CX + 200, CY - 80, -0.6, 60, 3, CYAN)
end

# 02 Hidden Curriculum: a visible lattice with the real network faint beneath it.
MOTIFS[2] = lambda do |svg, rng, accent|
  4.times do |r|
    6.times do |c|
      x = CX - 250 + c * 100
      y = CY - 110 + r * 74
      svg.rect(x - 26, y - 16, 52, 32, rx: 6, stroke: INK, sw: 1.6, opacity: 0.35)
    end
  end
  hidden = Array.new(9) { [CX - 240 + rng.rand(480), CY - 100 + rng.rand(220)] }
  hidden.combination(2) do |(a, b)|
    next if (a[0] - b[0]).abs + (a[1] - b[1]).abs > 330

    svg.line(a[0], a[1], b[0], b[1], stroke: accent, sw: 2.4, opacity: 0.5, dash: "1 9")
  end
  hidden.each { |(x, y)| svg.circle(x, y, 6, fill: accent, opacity: 0.9) }
  svg.circle(hidden[0][0], hidden[0][1], 13, stroke: CYAN, sw: 2.5, opacity: 0.9)
end

# 03 Python & Jupyter: notebook cells with a prompt chevron and a result sparkline.
MOTIFS[3] = lambda do |svg, rng, accent|
  [[-120, 92, false], [-8, 64, true], [76, 92, false]].each do |(dy, h, active)|
    y = CY + dy - h / 2
    svg.rect(CX - 250, y, 500, h, rx: 10,
             fill: active ? accent : "none", stroke: active ? accent : INK,
             sw: 2, opacity: active ? 0.16 : 0.5)
    svg.rect(CX - 250, y, 500, h, rx: 10, stroke: active ? accent : INK, sw: 2, opacity: active ? 0.9 : 0.5)
    svg.path("M #{CX - 232} #{y + h / 2 - 9} l 12 9 l -12 9", stroke: active ? accent : INK, sw: 3, opacity: 0.9)
    2.times do |i|
      svg.line(CX - 200, y + h * (0.36 + 0.3 * i), CX - 200 + 150 + rng.rand(160), y + h * (0.36 + 0.3 * i),
               stroke: INK, sw: 4, opacity: active ? 0.7 : 0.35)
    end
  end
  d = "M #{CX + 90} #{CY + 104}"
  9.times { |i| d += " L #{CX + 90 + (i + 1) * 17} #{CY + 104 - 10 - rng.rand(34)}" }
  svg.path(d, stroke: CYAN, sw: 3, opacity: 0.95)
end

# 04 Neuroanatomy: a soma with a full dendritic arbor and one long axon.
MOTIFS[4] = lambda do |svg, rng, accent|
  soma(svg, CX - 150, CY + 30, 44, accent)
  branch(svg, rng, CX - 168, CY - 8, -1.9, 84, 5, accent)
  branch(svg, rng, CX - 110, CY - 4, -0.7, 78, 5, accent)
  branch(svg, rng, CX - 186, CY + 62, 2.6, 66, 4, accent)
  # Axon with boutons.
  d = "M #{CX - 108} #{CY + 44} C #{CX + 20} #{CY + 90}, #{CX + 120} #{CY + 20}, #{CX + 290} #{CY + 52}"
  svg.path(d, stroke: CYAN, sw: 4, opacity: 0.95)
  [[CX + 40, CY + 62], [CX + 150, CY + 33], [CX + 250, CY + 45]].each do |(x, y)|
    svg.circle(x, y, 8, fill: CYAN, opacity: 0.9)
  end
end

# 05 EM & Image Basics: a beam cone scanning a circular field with raster lines.
MOTIFS[5] = lambda do |svg, rng, accent|
  svg.poly([[CX, CY - 190], [CX - 66, CY - 44], [CX + 66, CY - 44]], fill: accent, opacity: 0.25)
  svg.line(CX, CY - 190, CX - 66, CY - 44, stroke: accent, sw: 2.5, opacity: 0.9)
  svg.line(CX, CY - 190, CX + 66, CY - 44, stroke: accent, sw: 2.5, opacity: 0.9)
  svg.circle(CX, CY + 46, 128, stroke: INK, sw: 3, opacity: 0.85)
  svg.circle(CX, CY + 46, 128, fill: accent, opacity: 0.08)
  10.times do |i|
    y = CY - 62 + i * 24
    half = Math.sqrt([128**2 - (y - (CY + 46))**2, 0].max)
    next if half < 10

    svg.line(CX - half + 6, y, CX + half - 6, y, stroke: INK, sw: 1.6, opacity: 0.4)
  end
  # Membrane-like profiles inside the field.
  svg.circle(CX - 42, CY + 30, 26, stroke: CYAN, sw: 2.5, opacity: 0.85)
  svg.circle(CX + 38, CY + 78, 34, stroke: CYAN, sw: 2.5, opacity: 0.85)
  svg.circle(CX + 34, CY + 8, 15, stroke: INK, sw: 2, opacity: 0.6)
end

# 06 Segmentation 101: a tile mosaic, one region flood-filled across tiles.
MOTIFS[6] = lambda do |svg, rng, accent|
  filled = [[1, 1], [2, 1], [2, 2], [3, 2], [1, 2]]
  5.times do |r|
    7.times do |c|
      x = CX - 245 + c * 70
      y = CY - 145 + r * 58
      on = filled.include?([r, c])
      svg.rect(x, y, 64, 52, rx: 5,
               fill: on ? accent : "none",
               stroke: on ? accent : INK, sw: on ? 2.5 : 1.4,
               opacity: on ? 0.55 : 0.35)
    end
  end
  d = "M #{CX - 175} #{CY - 60} C #{CX - 60} #{CY - 110}, #{CX + 40} #{CY - 10}, #{CX + 45} #{CY + 25}"
  svg.path(d, stroke: INK, sw: 3.5, opacity: 0.9)
end

# 07 Proofreading & QC: a lens over a process, a split mark and a merge mark.
MOTIFS[7] = lambda do |svg, rng, accent|
  d = "M #{CX - 290} #{CY + 10} C #{CX - 150} #{CY - 60}, #{CX - 40} #{CY + 70}, #{CX + 120} #{CY - 10}"
  svg.path(d, stroke: CYAN, sw: 5, opacity: 0.8)
  d2 = "M #{CX + 120} #{CY - 10} C #{CX + 190} #{CY - 46}, #{CX + 240} #{CY - 20}, #{CX + 296} #{CY - 40}"
  svg.path(d2, stroke: CYAN, sw: 5, opacity: 0.35, dash: "10 8")
  svg.circle(CX + 30, CY + 22, 66, stroke: accent, sw: 5, opacity: 0.95)
  svg.circle(CX + 30, CY + 22, 66, fill: accent, opacity: 0.10)
  svg.line(CX + 78, CY + 70, CX + 130, CY + 122, stroke: accent, sw: 9, opacity: 0.95)
  # Inside the lens: the boundary question.
  svg.line(CX + 2, CY + 22, CX + 60, CY + 22, stroke: INK, sw: 3, opacity: 0.9)
  svg.line(CX + 30, CY - 4, CX + 30, CY + 48, stroke: accent, sw: 3, opacity: 0.9, dash: "6 6")
  svg.circle(CX - 180, CY - 22, 9, stroke: accent, sw: 3)
  svg.line(CX - 187, CY - 29, CX - 173, CY - 15, stroke: accent, sw: 3)
end

# 08 Hypothesis Testing: observed value against a null distribution.
MOTIFS[8] = lambda do |svg, rng, accent|
  base = CY + 110
  svg.line(CX - 280, base, CX + 280, base, stroke: INK, sw: 2.5, opacity: 0.7)
  d = "M #{CX - 260} #{base}"
  61.times do |i|
    x = -260 + i * 8
    yy = 190 * Math.exp(-((x + 40)**2) / 9000.0)
    d += " L #{CX + x} #{base - yy}"
  end
  svg.path(d, stroke: INK, sw: 3, opacity: 0.75)
  svg.path(d + " L #{CX + 220} #{base} Z", fill: INK, opacity: 0.08)
  svg.line(CX + 150, base, CX + 150, base - 200, stroke: accent, sw: 5, opacity: 0.95)
  svg.circle(CX + 150, base - 200, 9, fill: accent)
  svg.path("M #{CX + 150} #{base - 148} C #{CX + 90} #{base - 190}, #{CX + 30} #{base - 190}, #{CX - 20} #{base - 165}",
           stroke: accent, sw: 2.5, opacity: 0.7, dash: "7 7")
end

# 09 Morphology & Skeletonization: a filled arbor and its centerline twin.
MOTIFS[9] = lambda do |svg, rng, accent|
  soma(svg, CX - 210, CY, 38, CYAN, opacity: 0.9)
  branch(svg, Random.new(9), CX - 190, CY - 24, -1.1, 80, 4, CYAN)
  branch(svg, Random.new(10), CX - 180, CY + 22, 0.5, 72, 4, CYAN)
  arrow(svg, CX - 40, CY, CX + 40, CY, INK, sw: 3, opacity: 0.7)
  # Skeleton: same topology as dots and thin lines.
  nodes = [[CX + 110, CY], [CX + 160, CY - 46], [CX + 210, CY - 82], [CX + 205, CY - 10],
           [CX + 160, CY + 44], [CX + 214, CY + 76], [CX + 258, CY - 108], [CX + 262, CY + 44]]
  edges = [[0, 1], [1, 2], [1, 3], [0, 4], [4, 5], [2, 6], [5, 7]]
  edges.each { |(a, b)| svg.line(nodes[a][0], nodes[a][1], nodes[b][0], nodes[b][1], stroke: accent, sw: 2.5, opacity: 0.9) }
  nodes.each { |(x, y)| svg.circle(x, y, 5.5, fill: accent) }
  svg.circle(CX + 110, CY, 10, stroke: accent, sw: 3)
end

# 10 Network Science: a graph with one motif triangle lit up.
MOTIFS[10] = lambda do |svg, rng, accent|
  nodes = Array.new(11) { [CX - 240 + rng.rand(480), CY - 130 + rng.rand(260)] }
  nodes.combination(2) do |(a, b)|
    dx = (a[0] - b[0]).abs
    dy = (a[1] - b[1]).abs
    next if dx + dy > 300 || rng.rand > 0.6

    svg.line(a[0], a[1], b[0], b[1], stroke: INK, sw: 1.8, opacity: 0.35)
  end
  tri = [nodes[1], nodes[4], nodes[7]]
  tri.combination(2) { |(a, b)| svg.line(a[0], a[1], b[0], b[1], stroke: accent, sw: 4, opacity: 0.95) }
  nodes.each_with_index do |(x, y), i|
    hot = [1, 4, 7].include?(i)
    svg.circle(x, y, hot ? 10 : 6, fill: hot ? accent : INK, opacity: hot ? 1 : 0.65)
  end
end

# 11 Synapses & Circuit Logic: two apposed boutons, vesicles, and the cleft.
MOTIFS[11] = lambda do |svg, rng, accent|
  svg.path("M #{CX - 250} #{CY - 90} C #{CX - 90} #{CY - 130}, #{CX - 40} #{CY - 60}, #{CX - 38} #{CY}
             C #{CX - 40} #{CY + 60}, #{CX - 120} #{CY + 90}, #{CX - 250} #{CY + 70}",
           stroke: CYAN, sw: 4, opacity: 0.9)
  12.times do
    svg.circle(CX - 150 + rng.rand(88), CY - 55 + rng.rand(110), 7, stroke: INK, sw: 2, opacity: 0.8)
  end
  # Cleft.
  svg.line(CX - 16, CY - 66, CX - 16, CY + 66, stroke: accent, sw: 5, opacity: 0.9)
  svg.line(CX + 14, CY - 66, CX + 14, CY + 66, stroke: accent, sw: 10, opacity: 0.9)
  svg.path("M #{CX + 40} #{CY - 90} C #{CX + 180} #{CY - 120}, #{CX + 260} #{CY - 30}, #{CX + 268} #{CY + 10}
             C #{CX + 250} #{CY + 80}, #{CX + 140} #{CY + 96}, #{CX + 40} #{CY + 74}",
           stroke: accent, sw: 4, opacity: 0.9)
  arrow(svg, CX - 70, CY, CX + 60, CY, INK, sw: 2.5, opacity: 0.55)
end

# 12 Big Data: an isometric volume diced into chunks, one chunk pulled out.
MOTIFS[12] = lambda do |svg, rng, accent|
  iso = lambda do |x, y, z|
    [CX - 40 + (x - y) * 0.86 * 46, CY + 40 + (x + y) * 0.5 * 46 - z * 52]
  end
  cube = lambda do |x, y, z, color, opacity|
    top = [iso.(x, y, z + 1), iso.(x + 1, y, z + 1), iso.(x + 1, y + 1, z + 1), iso.(x, y + 1, z + 1)]
    left = [iso.(x, y + 1, z), iso.(x + 1, y + 1, z), iso.(x + 1, y + 1, z + 1), iso.(x, y + 1, z + 1)]
    right = [iso.(x + 1, y, z), iso.(x + 1, y + 1, z), iso.(x + 1, y + 1, z + 1), iso.(x + 1, y, z + 1)]
    svg.poly(top, fill: color, stroke: color, sw: 1.5, opacity: opacity * 0.45)
    svg.poly(left, fill: color, stroke: color, sw: 1.5, opacity: opacity * 0.22)
    svg.poly(right, fill: color, stroke: color, sw: 1.5, opacity: opacity * 0.30)
  end
  [0, 1, 2].each do |z|
    [0, 1, 2].each do |y|
      [0, 1, 2].each do |x|
        next if x == 2 && y.zero? && z == 2 # the extracted chunk

        cube.(x - 1.5, y - 1.5, z - 1.5, INK, 0.5)
      end
    end
  end
  cube.(1.7, -2.7, 1.3, accent, 2.0)
  svg.line(CX + 76, CY - 26, CX + 116, CY - 52, stroke: accent, sw: 2, opacity: 0.5, dash: "3 7")
end

# 13 Machine Learning: a small layered network, one path of weights lit.
MOTIFS[13] = lambda do |svg, rng, accent|
  layers = [[-220, 4], [-70, 6], [80, 6], [230, 2]]
  coords = layers.map do |(dx, n)|
    Array.new(n) { |i| [CX + dx, CY - (n - 1) * 27 + i * 54] }
  end
  coords.each_cons(2) do |from, to|
    from.each do |a|
      to.each do |b|
        svg.line(a[0], a[1], b[0], b[1], stroke: INK, sw: 1.2, opacity: 0.22)
      end
    end
  end
  lit = [coords[0][1], coords[1][2], coords[2][3], coords[3][0]]
  lit.each_cons(2) { |a, b| svg.line(a[0], a[1], b[0], b[1], stroke: accent, sw: 4, opacity: 0.95) }
  coords.flatten(1).each { |(x, y)| svg.circle(x, y, 9, fill: GROUND_B, stroke: INK, sw: 2, opacity: 0.9) }
  lit.each { |(x, y)| svg.circle(x, y, 9, fill: accent) }
end

# 14 Computer Vision for EM: an image grid with a convolution window sliding.
MOTIFS[14] = lambda do |svg, rng, accent|
  8.times do |r|
    12.times do |c|
      x = CX - 264 + c * 44
      y = CY - 152 + r * 38
      svg.rect(x, y, 40, 34, rx: 3, fill: INK, opacity: 0.05 + rng.rand * 0.11)
    end
  end
  svg.rect(CX - 264 + 3 * 44 - 4, CY - 152 + 2 * 38 - 4, 44 * 3, 38 * 3, rx: 6,
           stroke: accent, sw: 4, opacity: 0.95)
  svg.rect(CX - 264 + 3 * 44 - 4, CY - 152 + 2 * 38 - 4, 44 * 3, 38 * 3, fill: accent, opacity: 0.15)
  arrow(svg, CX + 40, CY - 40, CX + 130, CY - 40, accent, sw: 3)
  svg.rect(CX + 160, CY - 74, 68, 68, rx: 6, stroke: CYAN, sw: 3, opacity: 0.9)
  svg.circle(CX + 194, CY - 40, 16, fill: CYAN, opacity: 0.6)
end

# 15 LLMs for Patch Analysis: an EM patch beside token bars in conversation.
MOTIFS[15] = lambda do |svg, rng, accent|
  svg.rect(CX - 270, CY - 100, 200, 200, rx: 12, stroke: INK, sw: 3, opacity: 0.8)
  svg.circle(CX - 205, CY - 35, 30, stroke: CYAN, sw: 2.5, opacity: 0.8)
  svg.circle(CX - 130, CY + 30, 40, stroke: CYAN, sw: 2.5, opacity: 0.8)
  svg.circle(CX - 118, CY - 52, 16, stroke: INK, sw: 2, opacity: 0.5)
  arrow(svg, CX - 40, CY, CX + 30, CY, INK, sw: 3, opacity: 0.7)
  svg.rect(CX + 60, CY - 96, 240, 88, rx: 14, stroke: accent, sw: 3, opacity: 0.9)
  svg.poly([[CX + 100, CY - 8], [CX + 124, CY - 8], [CX + 96, CY + 16]], fill: accent, opacity: 0.9)
  [0, 1].each do |i|
    svg.line(CX + 84, CY - 72 + i * 26, CX + 84 + 120 + rng.rand(70), CY - 72 + i * 26,
             stroke: accent, sw: 6, opacity: 0.75)
  end
  svg.rect(CX + 90, CY + 40, 210, 62, rx: 14, stroke: INK, sw: 2.5, opacity: 0.6)
  svg.line(CX + 112, CY + 62, CX + 262, CY + 62, stroke: INK, sw: 5, opacity: 0.5)
  svg.line(CX + 112, CY + 82, CX + 202, CY + 82, stroke: INK, sw: 5, opacity: 0.5)
end

# 16 Scientific Visualization: honest axes, a labeled-feeling line, an error band.
MOTIFS[16] = lambda do |svg, rng, accent|
  ox = CX - 220
  oy = CY + 120
  svg.line(ox, oy, ox + 460, oy, stroke: INK, sw: 3, opacity: 0.85)
  svg.line(ox, oy, ox, oy - 250, stroke: INK, sw: 3, opacity: 0.85)
  5.times { |i| svg.line(ox + 90 * (i + 1), oy, ox + 90 * (i + 1), oy - 240, stroke: INK, sw: 1, opacity: 0.12) }
  pts = 9.times.map { |i| [ox + 30 + i * 50, oy - 40 - i * 18 - rng.rand(26)] }
  band_top = pts.map { |(x, y)| "#{x},#{y - 22}" }.join(" ")
  band_bot = pts.reverse.map { |(x, y)| "#{x},#{y + 22}" }.join(" ")
  svg << %(<polygon points="#{band_top} #{band_bot}" fill="#{accent}" opacity="0.16"/>)
  pts.each_cons(2) { |a, b| svg.line(a[0], a[1], b[0], b[1], stroke: accent, sw: 4, opacity: 0.95) }
  pts.each { |(x, y)| svg.circle(x, y, 5.5, fill: INK) }
end

# 17 Scientific Writing: a manuscript taking shape, heading then argument bars.
MOTIFS[17] = lambda do |svg, rng, accent|
  svg.rect(CX - 160, CY - 150, 320, 300, rx: 10, stroke: INK, sw: 3, opacity: 0.8)
  svg.line(CX - 128, CY - 110, CX + 60, CY - 110, stroke: accent, sw: 9, opacity: 0.95)
  [[-70, 1], [-46, 0.9], [-22, 0.95], [2, 0.55], [40, 0.9], [64, 0.8], [88, 0.4]].each do |(dy, len)|
    svg.line(CX - 128, CY + dy, CX - 128 + 256 * len, CY + dy, stroke: INK, sw: 4, opacity: 0.5)
  end
  # Margin note and its arrow into the text.
  svg.rect(CX + 190, CY - 60, 110, 64, rx: 8, stroke: accent, sw: 2.5, opacity: 0.9)
  svg.line(CX + 206, CY - 38, CX + 284, CY - 38, stroke: accent, sw: 4, opacity: 0.7)
  svg.line(CX + 206, CY - 18, CX + 260, CY - 18, stroke: accent, sw: 4, opacity: 0.7)
  arrow(svg, CX + 190, CY - 28, CX + 134, CY + 2, accent, sw: 2.5)
end

# 18 Data Cleaning: scattered noise passing a sieve into aligned rows.
MOTIFS[18] = lambda do |svg, rng, accent|
  26.times do
    svg.circle(CX - 280 + rng.rand(200), CY - 130 + rng.rand(260), 3 + rng.rand * 4,
               fill: INK, opacity: 0.28 + rng.rand * 0.3)
  end
  svg.line(CX - 30, CY - 140, CX - 30, CY + 140, stroke: accent, sw: 5, opacity: 0.9)
  3.times { |i| svg.line(CX - 30, CY - 90 + i * 90, CX + 6, CY - 90 + i * 90, stroke: accent, sw: 3, opacity: 0.7) }
  4.times do |r|
    6.times do |c|
      svg.circle(CX + 70 + c * 40, CY - 84 + r * 56, 5, fill: CYAN, opacity: 0.9)
    end
  end
end

# 19 Peer Review & Ethics: two manuscripts exchanging annotated passes.
MOTIFS[19] = lambda do |svg, rng, accent|
  [[-180, INK], [120, accent]].each do |(dx, color)|
    svg.rect(CX + dx - 60, CY - 90, 140, 180, rx: 10, stroke: color, sw: 3, opacity: 0.85)
    4.times do |i|
      svg.line(CX + dx - 36, CY - 52 + i * 34, CX + dx + 52, CY - 52 + i * 34, stroke: color, sw: 3.5, opacity: 0.45)
    end
  end
  svg.path("M #{CX - 96} #{CY - 110} C #{CX - 20} #{CY - 170}, #{CX + 80} #{CY - 170}, #{CX + 140} #{CY - 112}",
           stroke: accent, sw: 3.5, opacity: 0.9)
  arrow(svg, CX + 130, CY - 122, CX + 140, CY - 112, accent, sw: 3.5)
  svg.path("M #{CX + 96} #{CY + 110} C #{CX + 20} #{CY + 170}, #{CX - 80} #{CY + 170}, #{CX - 140} #{CY + 112}",
           stroke: INK, sw: 3.5, opacity: 0.7)
  arrow(svg, CX - 130, CY + 122, CX - 140, CY + 112, INK, sw: 3.5)
  svg.path("M #{CX + 146} #{CY + 34} l 12 14 l 24 -28", stroke: CYAN, sw: 5, opacity: 0.95)
end

# 20 Statistical Models: two overlapping distributions and the effect gap.
MOTIFS[20] = lambda do |svg, rng, accent|
  base = CY + 110
  svg.line(CX - 280, base, CX + 280, base, stroke: INK, sw: 2.5, opacity: 0.7)
  draw_curve = lambda do |center, height, color, fill_opacity|
    d = "M #{CX - 280} #{base}"
    71.times do |i|
      x = -280 + i * 8
      yy = height * Math.exp(-((x - center)**2) / 7200.0)
      d += " L #{CX + x} #{base - yy}"
    end
    svg.path(d, stroke: color, sw: 3.5, opacity: 0.9)
    svg.path(d + " L #{CX + 280} #{base} Z", fill: color, opacity: fill_opacity)
  end
  draw_curve.(-90, 180, INK, 0.10)
  draw_curve.(70, 205, accent, 0.16)
  svg.line(CX - 90, base - 190, CX - 90, base - 226, stroke: INK, sw: 2.5, opacity: 0.8)
  svg.line(CX + 70, base - 215, CX + 70, base - 226, stroke: accent, sw: 2.5, opacity: 0.9)
  svg.line(CX - 90, base - 226, CX + 70, base - 226, stroke: CYAN, sw: 3, opacity: 0.95)
  [[CX - 90], [CX + 70]].each { |(x)| svg.circle(x, base - 226, 4.5, fill: CYAN) }
end

# 21 Reproducibility & FAIR: a pipeline whose stages are openly linked and keyed.
MOTIFS[21] = lambda do |svg, rng, accent|
  xs = [CX - 240, CX - 80, CX + 80, CX + 240]
  xs.each_cons(2) do |a, b|
    svg.line(a + 44, CY, b - 44, CY, stroke: accent, sw: 3.5, opacity: 0.85)
    svg.circle((a + b) / 2.0, CY, 7, stroke: accent, sw: 3, opacity: 0.95)
  end
  xs.each_with_index do |x, i|
    svg.rect(x - 44, CY - 44, 88, 88, rx: 12, stroke: i == 3 ? CYAN : INK, sw: 3, opacity: 0.85)
    svg.rect(x - 44, CY - 44, 88, 88, rx: 12, fill: accent, opacity: 0.08)
    # An open latch on each stage: findable, openable.
    svg.path("M #{x - 12} #{CY - 6} a 12 12 0 0 1 24 0", stroke: INK, sw: 3, opacity: 0.8)
    svg.rect(x - 16, CY - 6, 32, 24, rx: 4, stroke: INK, sw: 3, opacity: 0.8)
  end
  svg.line(CX - 240, CY + 78, CX + 240, CY + 78, stroke: INK, sw: 2, opacity: 0.4, dash: "2 8")
end

# 22 Writing & Presentation: a speaker point with widening arcs reaching listeners.
MOTIFS[22] = lambda do |svg, rng, accent|
  svg.circle(CX - 220, CY, 16, fill: accent)
  3.times do |i|
    r = 70 + i * 62
    svg.path("M #{CX - 220 + r * 0.5} #{CY - r * 0.87} A #{r} #{r} 0 0 1 #{CX - 220 + r * 0.5} #{CY + r * 0.87}",
             stroke: accent, sw: 3.5 - i * 0.7, opacity: 0.9 - i * 0.22)
  end
  listeners = [[CX + 90, CY - 90], [CX + 160, CY - 20], [CX + 110, CY + 70], [CX + 230, CY + 46], [CX + 240, CY - 78]]
  listeners.each do |(x, y)|
    svg.circle(x, y, 10, stroke: INK, sw: 3, opacity: 0.85)
    svg.circle(x, y, 10, fill: CYAN, opacity: 0.25)
  end
  listeners.each_cons(2) { |a, b| svg.line(a[0], a[1], b[0], b[1], stroke: INK, sw: 1.6, opacity: 0.3) }
end

# 23 Posters & Conferences: a poster wall, one panel drawing a crowd of dots.
MOTIFS[23] = lambda do |svg, rng, accent|
  svg.rect(CX - 200, CY - 150, 400, 210, rx: 10, stroke: INK, sw: 3, opacity: 0.85)
  svg.line(CX - 170, CY - 116, CX + 40, CY - 116, stroke: accent, sw: 8, opacity: 0.95)
  svg.rect(CX - 170, CY - 92, 172, 120, rx: 6, stroke: accent, sw: 2.5, opacity: 0.85)
  pts = 7.times.map { |i| [CX - 156 + i * 22, CY - 6 - rng.rand(70)] }
  pts.each_cons(2) { |a, b| svg.line(a[0], a[1], b[0], b[1], stroke: accent, sw: 3, opacity: 0.9) }
  svg.rect(CX + 22, CY - 92, 148, 54, rx: 6, stroke: INK, sw: 2, opacity: 0.6)
  svg.rect(CX + 22, CY - 22, 148, 50, rx: 6, stroke: INK, sw: 2, opacity: 0.6)
  [[CX - 120, CY + 110], [CX - 60, CY + 130], [CX + 10, CY + 116], [CX + 90, CY + 134], [CX + 150, CY + 112]].each do |(x, y)|
    svg.circle(x, y, 11, stroke: CYAN, sw: 3, opacity: 0.85)
  end
end

# 24 Career Pathways: one path forking into branches, each with its own milestone.
MOTIFS[24] = lambda do |svg, rng, accent|
  svg.path("M #{CX - 280} #{CY + 110} C #{CX - 160} #{CY + 100}, #{CX - 120} #{CY + 40}, #{CX - 40} #{CY + 10}",
           stroke: INK, sw: 5, opacity: 0.85)
  forks = [
    ["C #{CX + 60} #{CY - 40}, #{CX + 140} #{CY - 90}, #{CX + 250} #{CY - 110}", accent],
    ["C #{CX + 80} #{CY + 0}, #{CX + 170} #{CY - 10}, #{CX + 260} #{CY - 10}", CYAN],
    ["C #{CX + 60} #{CY + 50}, #{CX + 150} #{CY + 90}, #{CX + 245} #{CY + 105}", INK],
  ]
  forks.each do |(seg, color)|
    svg.path("M #{CX - 40} #{CY + 10} #{seg}", stroke: color, sw: 4, opacity: 0.9)
  end
  svg.circle(CX - 40, CY + 10, 9, fill: INK)
  [[CX + 250, CY - 110, accent], [CX + 260, CY - 10, CYAN], [CX + 245, CY + 105, INK]].each do |(x, y, color)|
    svg.circle(x, y, 11, stroke: color, sw: 3.5)
    svg.circle(x, y, 4.5, fill: color)
  end
  [[CX - 200, CY + 106], [CX - 110, CY + 62]].each { |(x, y)| svg.circle(x, y, 6, stroke: INK, sw: 2.5, opacity: 0.7) }
end

# 25 Portfolio & Final Project: artifacts orbiting, converging into one center.
MOTIFS[25] = lambda do |svg, rng, accent|
  svg.circle(CX, CY, 44, stroke: accent, sw: 4, opacity: 0.95)
  svg.circle(CX, CY, 44, fill: accent, opacity: 0.15)
  svg.path("M #{CX - 14} #{CY} l 10 12 l 20 -24", stroke: accent, sw: 5, opacity: 0.95)
  8.times do |i|
    a = i * Math::PI / 4 + 0.3
    x = CX + 170 * Math.cos(a)
    y = CY + 130 * Math.sin(a)
    svg.line(CX + 52 * Math.cos(a), CY + 52 * Math.sin(a), x - 20 * Math.cos(a), y - 20 * Math.sin(a),
             stroke: INK, sw: 2, opacity: 0.4, dash: "3 7")
    case i % 4
    when 0 then svg.rect(x - 14, y - 17, 28, 34, rx: 4, stroke: INK, sw: 2.5, opacity: 0.85)
    when 1 then svg.circle(x, y, 13, stroke: CYAN, sw: 2.5, opacity: 0.85)
    when 2
      svg.rect(x - 16, y - 12, 32, 24, rx: 4, stroke: INK, sw: 2.5, opacity: 0.85)
      svg.path("M #{x - 10} #{y + 6} l 7 -9 l 6 4 l 7 -10", stroke: CYAN, sw: 2, opacity: 0.9)
    when 3
      svg.poly([[x, y - 14], [x + 13, y + 9], [x - 13, y + 9]], stroke: INK, sw: 2.5, opacity: 0.85)
    end
  end
end

# --- assembly ----------------------------------------------------------------

def xml_escape(text)
  text.gsub("&", "&amp;").gsub("<", "&lt;").gsub(">", "&gt;")
end

def render_banner(out_path, seed:, accent:, label:, motif:)
  svg = Svg.new
  rng = Random.new(seed)
  ground(svg, rng, accent)
  motif.call(svg, rng, accent)

  label = xml_escape(label)
  content = <<~SVG
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 #{W} #{H}" role="img" aria-label="#{label}">
    <title>#{label}</title>
    #{defs(accent)}
    #{svg}
    </svg>
  SVG
  out_path.dirname.mkpath
  out_path.write(content)
end

modules = YAML.load_file(ROOT.join("_data/modules.yml"))
abort "expected 25 modules, got #{modules.size}" unless modules.size == 25

modules.each do |mod|
  n = mod["number"]
  render_banner(OUT_DIR.join(format("module%02d.svg", n)),
                seed: n * 7919,
                accent: STAGE_ACCENT.fetch(mod["stage"]),
                label: "Module #{format('%02d', n)}: #{mod['title']}",
                motif: MOTIFS.fetch(n))
end

puts "Generated #{modules.size} module art SVGs in #{OUT_DIR.relative_path_from(ROOT)}/"

# --- technical unit banners --------------------------------------------------
# Same visual system, one bespoke motif per unit, accent keyed to the unit's
# subject matter (imaging violet, proofreading red, glia green, ...).

UNIT_OUT = ROOT.join("assets/images/units")

UNIT_MOTIFS = {}

# 01 Why map the brain: an unresolved point cloud crossing a frontier into a crisp graph.
UNIT_MOTIFS["01-why-map-the-brain"] = lambda do |svg, rng, accent|
  26.times do
    svg.circle(CX - 280 + rng.rand(240), CY - 120 + rng.rand(240), 2.5 + rng.rand * 3,
               fill: INK, opacity: 0.18 + rng.rand * 0.25)
  end
  svg.line(CX - 10, CY - 150, CX - 10, CY + 150, stroke: accent, sw: 3, opacity: 0.7, dash: "10 8")
  nodes = Array.new(8) { [CX + 40 + rng.rand(240), CY - 110 + rng.rand(220)] }
  nodes.combination(2) do |(a, b)|
    next if (a[0] - b[0]).abs + (a[1] - b[1]).abs > 260 || rng.rand > 0.55
    svg.line(a[0], a[1], b[0], b[1], stroke: accent, sw: 2.2, opacity: 0.7)
  end
  nodes.each { |(x, y)| svg.circle(x, y, 6, fill: INK, opacity: 0.9) }
  arrow(svg, CX - 70, CY, CX + 30, CY, accent, sw: 3.5)
end

# 02 Brain data across scales: nested zoom frames, brain to circuit to vesicles.
UNIT_MOTIFS["02-brain-data-across-scales"] = lambda do |svg, rng, accent|
  svg.rect(CX - 290, CY - 130, 260, 260, rx: 16, stroke: INK, sw: 3, opacity: 0.8)
  svg.path("M #{CX - 250} #{CY + 40} C #{CX - 260} #{CY - 60}, #{CX - 130} #{CY - 90}, #{CX - 110} #{CY - 10}
            C #{CX - 100} #{CY + 60}, #{CX - 220} #{CY + 90}, #{CX - 250} #{CY + 40}",
           stroke: accent, sw: 3.5, opacity: 0.85)
  svg.rect(CX - 40, CY - 88, 176, 176, rx: 12, stroke: INK, sw: 3, opacity: 0.8)
  tri = [[CX + 4, CY - 40], [CX + 92, CY - 10], [CX + 30, CY + 52]]
  tri.combination(2) { |(a, b)| svg.line(a[0], a[1], b[0], b[1], stroke: accent, sw: 2.5, opacity: 0.85) }
  tri.each { |(x, y)| svg.circle(x, y, 6, fill: accent) }
  svg.rect(CX + 180, CY - 58, 116, 116, rx: 10, stroke: INK, sw: 3, opacity: 0.8)
  6.times { svg.circle(CX + 205 + rng.rand(66), CY - 34 + rng.rand(66), 7, stroke: accent, sw: 2.5, opacity: 0.9) }
  svg.line(CX - 30, CY - 130 + 32, CX - 40, CY - 88 + 20, stroke: INK, sw: 2, opacity: 0.5)
  svg.line(CX + 136, CY - 60, CX + 180, CY - 45, stroke: INK, sw: 2, opacity: 0.5)
end

# 03 EM prep and imaging: specimen block, section ribbon, beam onto a field.
UNIT_MOTIFS["03-em-prep-and-imaging"] = lambda do |svg, rng, accent|
  svg.poly([[CX - 290, CY - 40], [CX - 210, CY - 70], [CX - 150, CY - 40], [CX - 230, CY - 10]],
           fill: accent, opacity: 0.35)
  svg.poly([[CX - 290, CY - 40], [CX - 230, CY - 10], [CX - 230, CY + 60], [CX - 290, CY + 30]],
           fill: accent, opacity: 0.6)
  svg.poly([[CX - 230, CY - 10], [CX - 150, CY - 40], [CX - 150, CY + 30], [CX - 230, CY + 60]],
           fill: accent, opacity: 0.45)
  d = "M #{CX - 130} #{CY + 30}"
  6.times { |i| d += " q 25 #{i.even? ? -34 : 34} 50 0" }
  svg.path(d, stroke: INK, sw: 3, opacity: 0.75)
  5.times { |i| svg.rect(CX - 118 + i * 50, CY + 6, 26, 18, rx: 2, stroke: INK, sw: 2, opacity: 0.6) }
  svg.poly([[CX + 235, CY - 170], [CX + 195, CY - 60], [CX + 275, CY - 60]], fill: CYAN, opacity: 0.3)
  svg.circle(CX + 235, CY + 30, 88, stroke: CYAN, sw: 3, opacity: 0.9)
  5.times do |i|
    y = CY - 20 + i * 24
    half = Math.sqrt([88**2 - (y - (CY + 30))**2, 0].max)
    svg.line(CX + 235 - half + 6, y, CX + 235 + half - 6, y, stroke: INK, sw: 1.5, opacity: 0.4)
  end
end

# 04 Volume reconstruction infrastructure: tiles, aligned stack, served store.
UNIT_MOTIFS["04-volume-reconstruction-infrastructure"] = lambda do |svg, rng, accent|
  3.times do |r|
    3.times do |c|
      svg.rect(CX - 290 + c * 52, CY - 80 + r * 52, 46, 46, rx: 4, stroke: INK, sw: 2, opacity: 0.55)
    end
  end
  4.times do |i|
    svg.rect(CX - 80 + i * 7, CY - 74 + i * 12, 130, 26, rx: 5, stroke: accent, sw: 2.5, opacity: 0.85 - i * 0.12)
  end
  arrow(svg, CX - 120, CY, CX - 92, CY, INK, sw: 2.5, opacity: 0.6)
  cyl_x = CX + 190
  svg << %(<ellipse cx="#{cyl_x}" cy="#{CY - 60}" rx="72" ry="20" fill="none" stroke="#{accent}" stroke-width="3" opacity="0.9"/>)
  svg.line(cyl_x - 72, CY - 60, cyl_x - 72, CY + 60, stroke: accent, sw: 3, opacity: 0.9)
  svg.line(cyl_x + 72, CY - 60, cyl_x + 72, CY + 60, stroke: accent, sw: 3, opacity: 0.9)
  svg << %(<path d="M #{cyl_x - 72} #{CY + 60} A 72 20 0 0 0 #{cyl_x + 72} #{CY + 60}" fill="none" stroke="#{accent}" stroke-width="3" opacity="0.9"/>)
  2.times do |i|
    svg << %(<path d="M #{cyl_x - 72} #{CY - 20 + i * 40} A 72 20 0 0 0 #{cyl_x + 72} #{CY - 20 + i * 40}" fill="none" stroke="#{accent}" stroke-width="2" opacity="0.5"/>)
  end
  arrow(svg, CX + 78, CY, CX + 108, CY, INK, sw: 2.5, opacity: 0.6)
  svg.line(cyl_x, CY + 84, cyl_x, CY + 120, stroke: CYAN, sw: 3, opacity: 0.8)
  [[-60, 0], [0, 0], [60, 0]].each do |(dx, _)|
    svg.line(cyl_x, CY + 120, cyl_x + dx, CY + 150, stroke: CYAN, sw: 2.5, opacity: 0.7)
    svg.circle(cyl_x + dx, CY + 154, 4.5, fill: CYAN)
  end
end

# 05 Neuronal ultrastructure: inside a membrane profile - mitochondrion, vesicles, PSD.
UNIT_MOTIFS["05-neuronal-ultrastructure"] = lambda do |svg, rng, accent|
  svg.path("M #{CX - 290} #{CY - 120} C #{CX - 80} #{CY - 190}, #{CX + 200} #{CY - 150}, #{CX + 280} #{CY - 30}
            C #{CX + 320} #{CY + 60}, #{CX + 120} #{CY + 160}, #{CX - 90} #{CY + 140}
            C #{CX - 260} #{CY + 120}, #{CX - 340} #{CY - 30}, #{CX - 290} #{CY - 120}",
           stroke: accent, sw: 4, opacity: 0.9)
  svg << %(<ellipse cx="#{CX - 130}" cy="#{CY - 20}" rx="72" ry="38" fill="none" stroke="#{CYAN}" stroke-width="3" opacity="0.9" transform="rotate(-18 #{CX - 130} #{CY - 20})"/>)
  4.times do |i|
    svg.line(CX - 180 + i * 26, CY - 48 + i * 8, CX - 168 + i * 26, CY + 4 + i * 8, stroke: CYAN, sw: 2, opacity: 0.7)
  end
  10.times { svg.circle(CX + 60 + rng.rand(110), CY - 70 + rng.rand(90), 8, stroke: INK, sw: 2.2, opacity: 0.85) }
  svg.line(CX + 40, CY + 88, CX + 210, CY + 74, stroke: accent, sw: 10, opacity: 0.9)
  svg.line(CX + 40, CY + 108, CX + 210, CY + 94, stroke: INK, sw: 2, opacity: 0.5)
  svg.circle(CX - 40, CY + 70, 13, stroke: INK, sw: 2.2, opacity: 0.6)
  svg.circle(CX - 78, CY + 88, 9, stroke: INK, sw: 2.2, opacity: 0.6)
end

# 06 Axons and dendrites: spiny process vs beaded process, decision node between.
UNIT_MOTIFS["06-axons-and-dendrites"] = lambda do |svg, rng, accent|
  d1 = "M #{CX - 290} #{CY - 70} C #{CX - 130} #{CY - 110}, #{CX + 90} #{CY - 50}, #{CX + 290} #{CY - 90}"
  svg.path(d1, stroke: accent, sw: 6, opacity: 0.9)
  9.times do |i|
    t = 0.08 + i * 0.105
    x = CX - 290 + 580 * t
    y = CY - 70 - 32 * Math.sin(t * 3.1) - 8
    svg.line(x, y + 4, x + 4, y - 16, stroke: accent, sw: 2.5, opacity: 0.85)
    svg.circle(x + 5, y - 21, 5.5, fill: accent, opacity: 0.9)
  end
  d2 = "M #{CX - 290} #{CY + 80} C #{CX - 100} #{CY + 50}, #{CX + 80} #{CY + 110}, #{CX + 290} #{CY + 70}"
  svg.path(d2, stroke: CYAN, sw: 3.5, opacity: 0.9)
  [0.18, 0.42, 0.66, 0.88].each do |t|
    x = CX - 290 + 580 * t
    y = CY + 80 - 26 * Math.sin(t * 2.8) + 10 * t
    svg.circle(x, y - 3 * t, 11, fill: CYAN, opacity: 0.45)
    svg.circle(x, y - 3 * t, 11, stroke: CYAN, sw: 2.5, opacity: 0.9)
  end
  svg.circle(CX, CY, 15, stroke: INK, sw: 3, opacity: 0.9)
  svg.line(CX, CY - 15, CX, CY - 40, stroke: INK, sw: 2.5, opacity: 0.7)
  svg.line(CX, CY + 15, CX, CY + 40, stroke: INK, sw: 2.5, opacity: 0.7)
end

# 07 Glia: a star-form astrocyte with an endfoot wrapping a capillary.
UNIT_MOTIFS["07-glia"] = lambda do |svg, rng, accent|
  soma(svg, CX - 60, CY - 20, 34, accent)
  8.times do |i|
    a = i * Math::PI / 4 + 0.2
    branch(svg, Random.new(70 + i), CX - 60 + 36 * Math.cos(a), CY - 20 + 36 * Math.sin(a), a, 52, 3, accent)
  end
  svg.line(CX + 120, CY - 150, CX + 200, CY + 150, stroke: INK, sw: 26, opacity: 0.25, cap: "butt")
  svg.line(CX + 120, CY - 150, CX + 200, CY + 150, stroke: INK, sw: 26, opacity: 0.0, cap: "butt")
  svg.line(CX + 113, CY - 150, CX + 193, CY + 150, stroke: INK, sw: 3, opacity: 0.7)
  svg.line(CX + 133, CY - 150, CX + 213, CY + 150, stroke: INK, sw: 3, opacity: 0.7)
  svg.path("M #{CX + 26} #{CY - 6} C #{CX + 90} #{CY - 20}, #{CX + 118} #{CY - 26}, #{CX + 142} #{CY - 2}
            C #{CX + 150} #{CY + 16}, #{CX + 120} #{CY + 30}, #{CX + 104} #{CY + 16}",
           stroke: accent, sw: 4, opacity: 0.95)
  5.times { svg.circle(CX - 80 + rng.rand(60), CY - 50 + rng.rand(60), 3, fill: accent, opacity: 0.8) }
end

# 08 Segmentation and proofreading: two segments, a split cut, a merge bridge, a budget bar.
UNIT_MOTIFS["08-segmentation-and-proofreading"] = lambda do |svg, rng, accent|
  svg.path("M #{CX - 280} #{CY - 40} C #{CX - 180} #{CY - 100}, #{CX - 60} #{CY - 20}, #{CX + 30} #{CY - 60}",
           stroke: CYAN, sw: 14, opacity: 0.55)
  svg.path("M #{CX + 30} #{CY - 60} C #{CX + 120} #{CY - 100}, #{CX + 210} #{CY - 40}, #{CX + 285} #{CY - 70}",
           stroke: accent, sw: 14, opacity: 0.55)
  svg.line(CX + 22, CY - 100, CX + 42, CY - 22, stroke: INK, sw: 3.5, opacity: 0.95, dash: "8 6")
  svg.path("M #{CX - 150} #{CY - 62} C #{CX - 130} #{CY - 110}, #{CX - 60} #{CY - 110}, #{CX - 30} #{CY - 66}",
           stroke: accent, sw: 3, opacity: 0.8, dash: "3 6")
  svg.circle(CX - 90, CY - 96, 10, stroke: accent, sw: 3, opacity: 0.95)
  svg.line(CX - 97, CY - 103, CX - 83, CY - 89, stroke: accent, sw: 3, opacity: 0.95)
  svg.rect(CX - 200, CY + 70, 400, 26, rx: 13, stroke: INK, sw: 2.5, opacity: 0.7)
  svg.rect(CX - 200, CY + 70, 250, 26, rx: 13, fill: accent, opacity: 0.75)
  svg.line(CX + 50, CY + 58, CX + 50, CY + 108, stroke: INK, sw: 2.5, opacity: 0.9)
end

# 09 Connectome analysis and NeuroAI: adjacency matrix becoming a motif graph.
UNIT_MOTIFS["09-connectome-analysis-neuroai"] = lambda do |svg, rng, accent|
  6.times do |r|
    6.times do |c|
      x = CX - 280 + c * 36
      y = CY - 108 + r * 36
      filled = rng.rand < 0.3
      svg.rect(x, y, 32, 32, rx: 3,
               fill: filled ? accent : "none",
               stroke: INK, sw: 1.4,
               opacity: filled ? 0.6 : 0.3)
    end
  end
  arrow(svg, CX - 30, CY, CX + 40, CY, INK, sw: 3, opacity: 0.7)
  nodes = [[CX + 120, CY - 80], [CX + 230, CY - 60], [CX + 180, CY + 20], [CX + 100, CY + 60], [CX + 260, CY + 70]]
  [[0, 1], [1, 2], [0, 2], [2, 3], [2, 4], [3, 4]].each_with_index do |(a, b), i|
    hot = i < 3
    svg.line(nodes[a][0], nodes[a][1], nodes[b][0], nodes[b][1],
             stroke: hot ? accent : INK, sw: hot ? 4 : 2, opacity: hot ? 0.95 : 0.45)
  end
  nodes.each_with_index do |(x, y), i|
    hot = i < 3
    svg.circle(x, y, hot ? 9 : 6, fill: hot ? accent : INK, opacity: hot ? 1 : 0.6)
  end
end

# Atlas: a reference table with one row found, and a bookmark tab.
UNIT_MOTIFS["atlas-connectomics-reference"] = lambda do |svg, rng, accent|
  svg.rect(CX - 240, CY - 130, 480, 260, rx: 12, stroke: INK, sw: 3, opacity: 0.8)
  svg.line(CX - 240, CY - 84, CX + 240, CY - 84, stroke: INK, sw: 2.5, opacity: 0.7)
  [-100, 30, 160].each { |dx| svg.line(CX + dx, CY - 130, CX + dx, CY + 130, stroke: INK, sw: 1.5, opacity: 0.35) }
  [-40, 4, 48, 92].each do |dy|
    svg.line(CX - 240, CY + dy, CX + 240, CY + dy, stroke: INK, sw: 1.2, opacity: 0.25)
  end
  svg.rect(CX - 240, CY - 40, 480, 44, fill: accent, opacity: 0.3)
  svg.rect(CX - 240, CY - 40, 480, 44, stroke: accent, sw: 2.5, opacity: 0.9)
  svg.poly([[CX + 190, CY - 130], [CX + 222, CY - 130], [CX + 222, CY - 74], [CX + 206, CY - 90], [CX + 190, CY - 74]],
           fill: CYAN, opacity: 0.85)
  [[-220, -110], [-80, 50], [50, 180]].each_with_index do |(x1, x2), i|
    svg.line(CX + x1, CY - 18 - i * 0, CX + x2, CY - 18, stroke: INK, sw: 4, opacity: 0.7) if i.zero?
  end
end

UNITS = [
  ["01-why-map-the-brain", "Why Map the Brain", "#f59e0b",
   "an unresolved point cloud crossing a frontier line into a crisp measured graph"],
  ["02-brain-data-across-scales", "Brain Data Across Scales", "#2563eb",
   "three nested zoom frames, from brain outline to circuit to vesicles"],
  ["03-em-prep-and-imaging", "EM Prep and Imaging", "#7B68EE",
   "a specimen block, a ribbon of serial sections, and a beam scanning a circular field"],
  ["04-volume-reconstruction-infrastructure", "Volume Reconstruction Infrastructure", "#E67E22",
   "raw tiles aligning into a stack and flowing into a served data store"],
  ["05-neuronal-ultrastructure", "Neuronal Ultrastructure", "#4A90D9",
   "the inside of a membrane profile: a mitochondrion, a vesicle cluster, and a postsynaptic density"],
  ["06-axons-and-dendrites", "Axons and Dendrites", "#06b6d4",
   "a spiny process above and a beaded process below, with a decision node between them"],
  ["07-glia", "Glia", "#27AE60",
   "a star-shaped astrocyte extending an endfoot onto a capillary"],
  ["08-segmentation-and-proofreading", "Segmentation and Proofreading", "#E74C3C",
   "two segments meeting at a marked split, a dashed merge bridge, and a partly spent budget bar"],
  ["09-connectome-analysis-neuroai", "Connectome Analysis and NeuroAI", "#9B59B6",
   "an adjacency matrix becoming a graph with one motif highlighted"],
  ["atlas-connectomics-reference", "Atlas and Connectomics Reference", "#95A5A6",
   "a reference table with one row highlighted and a bookmark tab"],
].freeze

UNITS.each_with_index do |(slug, title, accent, _alt), i|
  render_banner(UNIT_OUT.join("#{slug}.svg"),
                seed: 104_729 + i * 7919,
                accent: accent,
                label: "Unit: #{title}",
                motif: UNIT_MOTIFS.fetch(slug))
end

puts "Generated #{UNITS.size} unit art SVGs in #{UNIT_OUT.relative_path_from(ROOT)}/"

# --- content-library banners -------------------------------------------------
# One banner per narrative entry. Entries share a motif family per section
# (accent = the section's tag-dimension color from the library index), with
# per-entry seeded variation in arrangement.

LIB_OUT = ROOT.join("assets/images/content-library")

FAMILY = {}

# Neuroanatomy: organelle profiles inside a curved membrane section.
FAMILY["neuroanatomy"] = lambda do |svg, rng, accent|
  svg.path("M #{CX - 300} #{CY - 100 - rng.rand(40)} C #{CX - 100} #{CY - 180}, #{CX + 180} #{CY - 140}, #{CX + 290} #{CY - 20}
            C #{CX + 330} #{CY + 70}, #{CX + 100} #{CY + 160}, #{CX - 110} #{CY + 130}
            C #{CX - 280} #{CY + 110}, #{CX - 350} #{CY - 20}, #{CX - 300} #{CY - 100}",
           stroke: accent, sw: 4, opacity: 0.9)
  (3 + rng.rand(2)).times do
    x = CX - 180 + rng.rand(340)
    y = CY - 70 + rng.rand(150)
    rot = rng.rand(360)
    rx = 30 + rng.rand(34)
    svg << %(<ellipse cx="#{x}" cy="#{y}" rx="#{rx}" ry="#{(rx * 0.55).round}" fill="none" stroke="#{CYAN}" stroke-width="2.6" opacity="0.85" transform="rotate(#{rot} #{x} #{y})"/>)
  end
  (6 + rng.rand(5)).times do
    svg.circle(CX - 160 + rng.rand(340), CY - 70 + rng.rand(150), 6 + rng.rand * 3, stroke: INK, sw: 2, opacity: 0.7)
  end
end

# Proofreading: a traced process with marked error sites.
FAMILY["proofreading"] = lambda do |svg, rng, accent|
  y0 = CY - 40 + rng.rand(60)
  d = "M #{CX - 300} #{y0}"
  x = CX - 300
  y = y0
  5.times do
    x2 = x + 100 + rng.rand(60)
    y2 = CY - 90 + rng.rand(180)
    d += " C #{x + 50} #{y}, #{x2 - 50} #{y2}, #{x2} #{y2}"
    x = x2
    y = y2
  end
  svg.path(d, stroke: CYAN, sw: 5, opacity: 0.8)
  (2 + rng.rand(2)).times do
    mx = CX - 180 + rng.rand(360)
    my = CY - 70 + rng.rand(140)
    if rng.rand < 0.5
      svg.line(mx - 12, my - 12, mx + 12, my + 12, stroke: accent, sw: 4, opacity: 0.95)
      svg.line(mx - 12, my + 12, mx + 12, my - 12, stroke: accent, sw: 4, opacity: 0.95)
    else
      svg.circle(mx, my, 15, stroke: accent, sw: 3.5, opacity: 0.95)
      svg.line(mx, my - 15, mx, my - 34, stroke: accent, sw: 3, opacity: 0.8)
    end
  end
  svg.circle(CX + 210, CY + 70, 44, stroke: accent, sw: 4, opacity: 0.9)
  svg.line(CX + 242, CY + 102, CX + 280, CY + 140, stroke: accent, sw: 7, opacity: 0.9)
end

# Connectomics: a graph with a community hull.
FAMILY["connectomics"] = lambda do |svg, rng, accent|
  nodes = Array.new(10 + rng.rand(4)) { [CX - 250 + rng.rand(500), CY - 120 + rng.rand(240)] }
  nodes.combination(2) do |(a, b)|
    next if (a[0] - b[0]).abs + (a[1] - b[1]).abs > 280 || rng.rand > 0.5
    svg.line(a[0], a[1], b[0], b[1], stroke: INK, sw: 1.8, opacity: 0.35)
  end
  hull = nodes.sample(3, random: rng)
  cxh = hull.sum { |p| p[0] } / 3.0
  cyh = hull.sum { |p| p[1] } / 3.0
  svg.circle(cxh, cyh, 78, stroke: accent, sw: 3, opacity: 0.55, dash: "6 8")
  hull.combination(2) { |(a, b)| svg.line(a[0], a[1], b[0], b[1], stroke: accent, sw: 3.5, opacity: 0.95) }
  nodes.each { |(x, y)| svg.circle(x, y, 5.5, fill: INK, opacity: 0.7) }
  hull.each { |(x, y)| svg.circle(x, y, 8.5, fill: accent) }
end

# Imaging: a raster field with artifact marks.
FAMILY["imaging"] = lambda do |svg, rng, accent|
  svg.rect(CX - 260, CY - 130, 520, 260, rx: 12, stroke: INK, sw: 3, opacity: 0.75)
  10.times do |i|
    svg.line(CX - 240, CY - 108 + i * 24, CX + 240, CY - 108 + i * 24, stroke: INK, sw: 1.4, opacity: 0.3)
  end
  (2 + rng.rand(2)).times do
    svg.circle(CX - 180 + rng.rand(360), CY - 80 + rng.rand(160), 18 + rng.rand(22), stroke: CYAN, sw: 2.5, opacity: 0.8)
  end
  fold_x = CX - 120 + rng.rand(240)
  svg.path("M #{fold_x} #{CY - 130} C #{fold_x + 24} #{CY - 40}, #{fold_x - 24} #{CY + 40}, #{fold_x} #{CY + 130}",
           stroke: accent, sw: 4, opacity: 0.9)
  svg.circle(CX - 200 + rng.rand(400), CY - 90 + rng.rand(180), 9, fill: accent, opacity: 0.7)
end

# Infrastructure: pipeline stages over a chunk grid.
FAMILY["infrastructure"] = lambda do |svg, rng, accent|
  n = 4
  xs = Array.new(n) { |i| CX - 240 + i * 160 }
  xs.each_cons(2) { |a, b| arrow(svg, a + 44, CY - 30, b - 44, CY - 30, accent, sw: 3) }
  xs.each do |x|
    svg.rect(x - 44, CY - 74, 88, 88, rx: 12, stroke: INK, sw: 3, opacity: 0.85)
    svg.rect(x - 44, CY - 74, 88, 88, rx: 12, fill: accent, opacity: 0.1)
  end
  hot = rng.rand(n)
  svg.rect(xs[hot] - 44, CY - 74, 88, 88, rx: 12, stroke: accent, sw: 3.5, opacity: 0.95)
  8.times do |i|
    svg.rect(CX - 180 + i * 46, CY + 70, 40, 34, rx: 4, stroke: INK, sw: 1.6, opacity: 0.3 + (i == hot * 2 ? 0.4 : 0))
  end
end

# Cell types: three distinct cell silhouettes in a row.
FAMILY["cell-types"] = lambda do |svg, rng, accent|
  soma(svg, CX - 180, CY, 34, accent)
  branch(svg, rng, CX - 196, CY - 28, -1.7, 62, 4, accent)
  branch(svg, rng, CX - 156, CY - 22, -0.6, 56, 4, accent)
  soma(svg, CX + 10, CY + 10, 26, CYAN, opacity: 0.9)
  6.times do |i|
    a = i * Math::PI / 3 + 0.3
    branch(svg, Random.new(200 + i), CX + 10 + 28 * Math.cos(a), CY + 10 + 28 * Math.sin(a), a, 40, 2, CYAN)
  end
  svg.circle(CX + 200, CY - 6, 24, fill: INK, opacity: 0.5)
  svg.circle(CX + 200, CY - 6, 30, stroke: INK, sw: 3, opacity: 0.85)
  [[-1, 1], [1, 1], [0, -1.3]].each do |(sx, sy)|
    svg.path("M #{CX + 200 + sx * 24} #{CY - 6 + sy * 18} q #{sx * 30} #{sy * 22} #{sx * 44} #{sy * 52}",
             stroke: INK, sw: 3, opacity: 0.75)
  end
end

# Case studies: a specimen ring with landmark points and a data band.
FAMILY["case-studies"] = lambda do |svg, rng, accent|
  svg.circle(CX - 80, CY, 110, stroke: accent, sw: 4, opacity: 0.9)
  svg.circle(CX - 80, CY, 110, fill: accent, opacity: 0.08)
  (3 + rng.rand(3)).times do
    a = rng.rand * Math::PI * 2
    r = 30 + rng.rand(70)
    svg.circle(CX - 80 + r * Math.cos(a), CY + r * Math.sin(a), 6, fill: INK, opacity: 0.85)
  end
  svg.circle(CX - 80 + rng.rand(60) - 30, CY + rng.rand(60) - 30, 12, stroke: CYAN, sw: 3, opacity: 0.95)
  4.times do |i|
    w = 60 + rng.rand(120)
    svg.line(CX + 90, CY - 54 + i * 36, CX + 90 + w, CY - 54 + i * 36, stroke: i.zero? ? accent : INK, sw: 7, opacity: i.zero? ? 0.9 : 0.45)
  end
end

# Section accents: the tag-dimension colors from the library index.
LIB_SECTIONS = {
  "neuroanatomy" => "#4A90D9",
  "imaging" => "#7B68EE",
  "infrastructure" => "#E67E22",
  "proofreading" => "#E74C3C",
  "cell-types" => "#27AE60",
  "connectomics" => "#F39C12",
  "case-studies" => "#1ABC9C",
}.freeze

LIB_ALT = {
  "neuroanatomy" => "organelle profiles inside a curved membrane section",
  "imaging" => "a raster imaging field crossed by artifact marks",
  "infrastructure" => "pipeline stages running above a chunk grid",
  "proofreading" => "a traced process with marked error sites under review",
  "cell-types" => "three cell silhouettes: branched, star-form, and amoeboid",
  "connectomics" => "a network graph with one community circled",
  "case-studies" => "a specimen ring with landmark points beside a data band",
}.freeze

library_count = 0
LIB_SECTIONS.each do |section, accent|
  Dir[ROOT.join("content-library", section, "*.md")].sort.each do |file|
    name = File.basename(file, ".md")
    front = File.read(file, encoding: "UTF-8")[/\A---\n(.*?)\n---/m, 1]
    title = front ? (YAML.safe_load(front, permitted_classes: [Date])["title"] || name) : name
    render_banner(LIB_OUT.join(section, "#{name}.svg"),
                  seed: (section + name).each_byte.reduce(17) { |h, b| h * 31 + b } % 2_147_483_647,
                  accent: accent,
                  label: title.to_s,
                  motif: FAMILY.fetch(section))
    library_count += 1
  end
end

puts "Generated #{library_count} content-library art SVGs in #{LIB_OUT.relative_path_from(ROOT)}/"
