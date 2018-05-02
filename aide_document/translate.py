from googletrans import Translator

def translate(src_filename, dest_filename, dest_lang, src_lang='auto'):
    """
    Converts a source file to a destination file in the selected language.

    Parameters
    ==========
    src_filename : String
        Relative file path to the original source file.
    dest_filename : String
        Relative file path to where the translated file should go.
    dest_lang : String
        The language of the destination file. Must be the correct 2-letter ISO-639-1 abbreviation from https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
    src_lang : String (OPTIONAL)
        The language of the source file. Only needed if the source file contains multiple languages. Like dest_lang, must be the correct ISO-639-1 abbreviation from https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
    
    Examples
    ========
    Suppose you have the following document in English:
    data/
        doc_en.md

    To translate it to Spanish:
    >>> from aide_document import translate
    >>> translate.translate('data/doc_en.md', 'data/doc_es.md', es, en)

    The last parameter can be omitted if the source file has only one language.
    """
    translator = Translator() # Initialize translator object

    with open(src_filename) as srcfile, open(dest_filename, 'w') as destfile:
        
        # Parses each line for special cases and ignores them when translating
        for line in srcfile.readlines():
            line = line.strip()

            # Parses for code blocks and ignores them
            if line.startswith("```"):
                line = line

            # Parses for URL's and file links and ignores them
            elif line.find("[") != -1 and line.find("]") != -1 and line.find("(") != -1 and line.find(")") != -1:
                ignore_start = line.find("(")
                ignore_end = line.find(")")
                head = translator.translate(line[0:ignore_start], dest_lang, src_lang).text
                tail = translator.translate(line[ignore_end+1:], dest_lang, src_lang).text
                line = head + line[ignore_start:ignore_end+1] + tail

            # Translates normally if there are no special cases
            else:
                line = translator.translate(line, dest_lang, src_lang).text

            # Write to destination file
            destfile.write(line + '\n')