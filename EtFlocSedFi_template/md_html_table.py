def parse(phrase,end,source):
    if source.startswith(end) is True:
        return phrase
    else:
        return parse(phrase+source[0],end,source[1:])

def cells(cell_line,elt):
    if len(elt) != 0:
        cell = parse("","|",elt)
        cell_line = cell_line + "\n    <th>" + cell.strip() + "</th>"
        return cells(cell_line,elt[len(cell)+1:])
    else:
        return cell_line

def md_html_table(filename, dest):
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    out = open(dest, "w")
    for elt in content:
        if elt.startswith("| **"):
            title = parse("","**",elt[4:])
            elt = str(
'''<tr>
    <th colspan="2">''')+str(title)+str('''"</th>
</tr>''')
            out.write(elt)
            out.write("\n")
        elif elt.startswith("| ----"):
            out.write("")
        elif elt.startswith("| "):
            line = cells("",elt[2:])
            elt = str('''<tr>''')+str(line)+str('''\n</tr>''')
            out.write(elt)
            out.write("\n")
        else:
            elt = elt
            out.write(elt)
            out.write("\n")
    out.close()

md_html_table("table.md","table_html.md")
