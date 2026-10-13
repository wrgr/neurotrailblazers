# Run after a Jekyll build. Exercises the shared resolver and its published surfaces.
require 'yaml'
require 'liquid'
require 'json'
root = File.expand_path('..', __dir__)
site = ENV.fetch('SITE_DIR', File.join(root, '_site'))
manifest = YAML.safe_load(File.read(File.join(root, '_data/module_status.yml')))
raise 'Unknown default module status' unless %w[unreviewed available in_development].include?(manifest['default_status'])
manifest.fetch('modules', {}).each do |slug, override|
  raise "Unknown module #{slug}" unless slug.match?(/\Amodule(?:0[1-9]|1\d|2[0-5])\z/)
  raise "Unknown status for #{slug}" unless %w[unreviewed available in_development].include?(override['status'])
end
source = File.read(File.join(root, '_includes/ui/module-status-value.html')) + '{{ module_state }}|{{ module_label }}'
template = Liquid::Template.parse(source)
fixtures = [
  [{ 'module_number'=>1, 'status'=>'active' }, {}, 'unreviewed|Status not confirmed'],
  [{ 'module_number'=>1, 'status'=>'draft' }, {}, 'in_development|In development'],
  [{ 'module_number'=>1, 'development_status'=>'planned', 'status'=>'active' }, {}, 'in_development|In development'],
  [{ 'number'=>1 }, {'module01'=>{'status'=>'available'}}, 'available|Available'],
  [{ 'url'=>'/teaching/sessions/module01/' }, {'module01'=>{'status'=>'in_development'}}, 'in_development|In development'],
  [{ 'module_number'=>1, 'status'=>'published' }, {}, 'available|Available'],
]
fixtures.each do |item, overrides, expected|
  actual = template.render!('include'=>{'item'=>item}, 'site'=>{'data'=>{'module_status'=>{'default_status'=>'unreviewed','modules'=>overrides}}}).strip
  raise "Resolver failed: #{actual.inspect} != #{expected.inspect}" unless actual == expected
end
index = JSON.parse(File.read(File.join(site, 'resources/search-index.json')))
raise 'Empty resource index' unless index.length > 100
raise 'Duplicate resource URLs' unless index.map{|p|p['url']}.uniq.length == index.length
modules = File.read(File.join(site,'modules/index.html'))
raise 'Module cards repeat' unless modules.scan(/class="card module-card"/).length == 25
(1..25).each do |number|
  slug = format('module%02d', number)
  state = manifest.fetch('modules', {}).dig(slug, 'status') || manifest['default_status']
  %W[modules/#{slug}/index.html teaching/sessions/#{slug}/index.html].each do |file|
    html = File.read(File.join(site, file))
    raise "Missing status in #{file}" unless html.include?("module-status-notice status-#{state}")
    if file.start_with?('modules/') && (2..9).include?(number)
      raise "Mismatched practice remains in #{file}" if html.include?('nt-task-submit')
      raise "Missing quiz remains required in #{file}" if html.match?(/data-step-index="[34]"/)
      raise "No development explanation in #{file}" unless html.include?('Interactive practice is being revised')
    end
  end
  %W[/modules/#{slug}/ /teaching/sessions/#{slug}/].each do |url|
    raise "Search has wrong status for #{url}" unless index.find{|p|p['url']==url}&.fetch('status') == state
  end
end
puts 'PASS usability: development status resolution, 25 module/session banners, searchable statuses, unique resource index'
