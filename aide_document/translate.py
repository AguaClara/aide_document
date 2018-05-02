from googletrans import Translator

def translate(src_filename, dest_filename, dest_lang, src_lang='auto'):
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
    translator = Translator()

    with open(src_filename) as srcfile, open(dest_filename, 'w') as destfile:
        
        # The following section parses the strings in the list to check if it belongs to a special case(link, image or code block).
        
        for line in srcfile.readlines():
            line = line.strip()
            # this if branch looks for code blocks and skip the url during translation
            if line.startswith("```"):
                line = line
            # this elif branch looks for links and images and skip the url during translation
            elif line.find("[") != -1 and line.find("]") != -1 and line.find("(") != -1 and line.find(")") != -1:
                pause1 = line.find("(")
                pause2 = line.find(")")
                head = translator.translate(line[0:pause1], dest_lang, src_lang).text
                tail = translator.translate(line[pause2+1:], dest_lang, src_lang).text
                line = head + line[pause1:pause2+1] + tail
            else:
                line = translator.translate(line, dest_lang, src_lang).text
            destfile.write(line + '\n')