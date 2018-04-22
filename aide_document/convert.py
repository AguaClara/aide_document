import os

def md_to_pdf(input_filename, output_filename):
    """
    md_to_pdf converts input_filename file to pdf,
    and the name of the pdf file is output_filename

    Parameters
    ----------
    input_filename : string
    name of file to convert to pdf

    output_filename : string
    name of the pdf file

    """

    os.system("pandoc " + input_filename + " -o " + output_filename + ".pdf" )

def docx_to_md(input_filename, output_filename):
    """
    docx_to_md converts input_filename file to md,
    and the name of the md file is output_filename

    Parameters
    ----------
    input_filename : string
    name of file to convert to pdf

    output_filename : string
    name of the pdf file

    """

    os.system("pandoc -s " + input_filename + " -t markdown -o " + output_filename + ".md" )

def pdf_to_md(input_filename, output_filename):
    """
    pdf_to_md converts input_filename file to markdown,
    and the name of the markdown file is output_filename

    Parameters
    ----------
    input_filename : string
    name of file to convert to pdf

    output_filename : string
    name of the pdf file

    """

    os.system("pandoc " + input_filename + " -o " + output_filename + ".md" )