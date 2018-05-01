import datetime

def add_frontmatter(file_name, title):
# TODO: add newfile when adding frontmatter
    with open(file_name, "r+") as f:
        content = f.read()
        f.seek(0)
        f.write('---\n' + 'title: ' + title + '\n' + '---\n')