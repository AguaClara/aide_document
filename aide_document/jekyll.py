def add_frontmatter(oldfile_name, title, makenew=False):
    with open(oldfile_name, "r+") as oldfile:
        if makenew:
            with open(oldfile_name[:-3] + '_added_frontmatter.md', 'w') as newfile:
                newfile.write('---\n' + 'title: ' + title + '\n' + '---\n')
                newfile.write(oldfile.read())
        else:
            content = oldfile.read()
            oldfile.seek(0)
            oldfile.write('---\n' + 'title: ' + title + '\n' + '---\n' + content)