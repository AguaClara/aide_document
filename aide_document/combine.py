import os
import yaml
from jinja2 import Environment, PackageLoader

def render_document(template_name, data_name, output_name):
    """
    Combines a MarkDown template file from the aide_document package with a local associated YAML data file, then outputs the rendered combination to a local MarkDown output file.

    Parameters
    ==========
    template_name : String
        Exact name of the MarkDown template file from the aide_document/templates folder. Do not use the file path.
    data_name : String
        Relative file path from where this method is called to the location of the YAML data file to be used.
    output_name : String
        Relative file path from where this method is called to the location to which the output file is written.
    
    Examples
    ========
    Suppose we have template.md in aide_document and a directory as follows:
    data/
        params.yaml

    To render the document:
    >>> from aide_document import combine
    >>> combine.render_document(template.md, data/params.yaml, data/output.md)

    This will then combine the data and template files and write to a new output file within data/.
    """
    # Set up environment and load templates from pip package
    env = Environment(loader=PackageLoader('aide_document'))

    # Create output file, open/render template and data files
    with open(output_name, 'w') as output_file:
        output = env.get_template(template_name).render(yaml.load(open(data_name)))
        output_file.write(output)