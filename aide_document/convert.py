import os

def md_to_pdf(input_name, output_name):
    """
    Converts an input MarkDown file to a PDF of the given output name.

    Parameters
    ==========
    input_name : String
    Relative file location of the input file to where this function is being called.

    output_name : String
    Relative file location of the output file to where this function is being called. Note that .pdf can be omitted.
    """
    if output_name[-4:] == '.pdf':
        os.system("pandoc " + input_name + " -o " + output_name)
    else:
        os.system("pandoc " + input_name + " -o " + output_name + ".pdf" )

def docx_to_md(input_name, output_name):
    """
    Converts an input docx file to MarkDown file of the given output name.

    Parameters
    ==========
    input_name : String
    Relative file location of the input file to where this function is being called.

    output_name : String
    Relative file location of the output file to where this function is being called. Note that .md can be omitted.
    """
    if output_name[-5:] == '.docx':
        os.system("pandoc " + input_name + " -o " + output_name)
    else:
        os.system("pandoc " + input_name + " -o " + output_name + ".docx" )