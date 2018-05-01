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
    #TODO: Add examples
    """
    with open(file_name, "r+") as oldfile:
        if makenew:
            with open(file_name[:-3] + '_added_frontmatter.md', 'w') as newfile:
                newfile.write('---\n' + 'title: ' + title + '\n' + '---\n')
                newfile.write(oldfile.read())
        else:
            content = oldfile.read()
            oldfile.seek(0)
            oldfile.write('---\n' + 'title: ' + title + '\n' + '---\n' + content)