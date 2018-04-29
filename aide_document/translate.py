from aide_document import google_trans


def translate(filename, src, tar, dest):
    """
    Converts an input MarkDown file to a PDF of the given output name.

    Parameters
    ==========
    [filename] : string
    The filename of the input file. Must be in the relative path.
    [src] : string
    The language of the input file content. Must be the correct abbreviation.
    [tar] : string
    The language of the output file content. Must be the correct abbreviation.
    [dest] : string
    The filename of the output file. It will appear in the relative path.
    """
    with open(filename) as f:
        content = f.readlines()

    content = [x.strip() for x in content]
    out = open(dest, "w")

    """
    The following section parses the strings in the list to check if it belongs
    to a special case(link, image or code block).
    """
    for elt in content:
        if elt.startswith("```"):
            elt = elt
        elif elt.find("(") != -1 and elt.find(")") != -1:
            pause1 = elt.find("(")
            pause2 = elt.find(")")
            head = google_trans.api(elt[0:pause1], src, tar)
            tail = google_trans.api(elt[pause2+1:], src, tar)
            elt = head + elt[pause1:pause2+1] + tail
        else:
            elt = google_trans.api(elt, src, tar)
        out.write(elt)
        out.write("\n")

    out.close()
