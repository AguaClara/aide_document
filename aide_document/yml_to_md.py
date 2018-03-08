import os
import yaml
from jinja2 import Environment, FileSystemLoader

# Function to render template from template environment and context
def render_template(template_filename, context):
    # Set up template environment from "templates" folder
    PATH = os.path.dirname(os.path.abspath(__file__))
    TEMPLATE_ENVIRONMENT = Environment(
        autoescape=False,
        loader=FileSystemLoader(os.path.join(PATH, 'templates')),
        trim_blocks=False)

    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

def render_documentation_template(input_name, output_name, template_name):
    # Declare output file and parameters
    context = yaml.load(open(input_name))

    # Making each value parse-able
    for key,value in context.items():
        context[key] = value

    # Final render
    with open(output_name, 'w') as f:
        output = render_template(template_name, context)
        f.write(output)

def to_pdf(input_file, output_file):
    """
    to_pdf converts a file into pdf

    Parameters
    ----------
    input_file : string
    name of file to convert to to pdf

    output_file : string
    name of the pdf file

    """

    os.system("pandoc " + input_file + " -o " + output_file + ".pdf" )
