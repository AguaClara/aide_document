import os
import yaml
import aide_design
from aide_design.units import unit_registry as u
from jinja2 import Environment, FileSystemLoader

# Render template from template environment and context
def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)
    
# Set up template environment from "templates" folder
PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)

# Declare output file and parameters
fname = "output.md"
context = yaml.load(file('input.yml'))

# Write to file from parameters and template
with open(fname, 'w') as f:
    html = render_template('example.md', context)
    f.write(html)