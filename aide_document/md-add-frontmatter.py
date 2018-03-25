import datetime

# Initial prompts for file info
try:
    title = raw_input('Name of file: ')
    old_file = open(title, "r")
except IOError:
    print("File not found! Did you spell the name correctly?")
    break
subteam = raw_input('Name of subteam: ')

# Adding tags
tags = []
tag = raw_input('Name of tag (leave blank if done): ')
while(tag != ''):
    tags.append(tag)
    tag = raw_input('Name of tag (leave blank if done): ')

# Open/create files to translate
new_file = open("output-file", "w+")

# Writing frontmatter
new_file.write("---\n")
new_file.write("title: " + title + "\n")
new_file.write("tags: [")
for i in range(len(tags)):
    new_file.write(tag)
    if (i != len(tags) - 1):
        new_file.write(',')
new_file.write("]\n")
new_file.write("keywords: tips, documentation theme, jekyll\n")
new_file.write("last_updated: " + str(datetime.datetime.now()) + "\n")
new_file.write("sidebar: api_sidebar\n")
new_file.write('summary: "This is the welcome page for AIDE Documentation"\n')
new_file.write("permalink: api_about.html\n")
new_file.write("---\n")

# Append old file to new file
new_file.write(old_file.read())

# Close files
new_file.close()
old_file.close()