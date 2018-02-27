import os
import yaml
from jinja2 import Environment, FileSystemLoader

# Function to render template from template environment and context
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

# Making each value parse-able
for key,value in context.items():
    context[key] = value

# Final render
with open(fname, 'w') as f:
    html = render_template('example.md', context)
    f.write(html)
