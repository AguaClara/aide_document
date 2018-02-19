import os
import yaml
from aide_design.units import unit_registry as u
from jinja2 import Environment, FileSystemLoader

# Set up template environment from "templates" folder
PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, 'templates')),
    trim_blocks=False)

# Render template from template environment and context
def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

# Pass through template file and parameters
def create_index_html():
    fname = "output.md"
    context = yaml.load(file('input.yml'))
    #
    with open(fname, 'w') as f:
        html = render_template('example.md', context)
        f.write(html)


def main():
    create_index_html()

########################################

if __name__ == "__main__":
    main()
