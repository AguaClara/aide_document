"""
Prepares documentation and sets up a Jekyll project into which the documentation goes.

Functions
=========
add_frontmatter(file_name, title, makenew=False)
    Adds basic frontmatter to a MarkDown file that will be used in a Jekyll project.
"""

def make_project

def add_frontmatter(file_name, title, makenew=False):
    """
    Adds basic frontmatter to a MarkDown file that will be used in a Jekyll project.

    Parameters
    ==========
    file_name : String
        Relative file path from where this method is called to the location of the file that will have frontmatter added.
    title : String
        Title of the page that will go into the Jekyll project.
    makenew : Boolean (OPTIONAL)
        If set to True, will create a new file with the frontmatter next to the original file with "_added_frontmatter" appended to its name. Otherwise, the method simply edits the original file.

    Examples
    ========
    Suppose we have the following directory:
    data/
        doc.md
    
    To write to a new file doc_add_frontmatter.md and add frontmatter:
    >>> from aide_document import jekyll
    >>> jekyll.add_frontmatter('doc.md', 'Document', True)

    The last parameter can be omitted if you want to just overwrite doc.md.
    """

    with open(file_name, "r+") as oldfile:

        # Creates new file and writes to it if specified
        if makenew:
            with open(file_name[:-3] + '_added_frontmatter.md', 'w') as newfile:
                newfile.write('---\n' + 'title: ' + title + '\n' + '---\n')
                newfile.write(oldfile.read())
        
        # Writes to old file if unspecified
        else:
            content = oldfile.read()
            oldfile.seek(0)
            oldfile.write('---\n' + 'title: ' + title + '\n' + '---\n' + content)