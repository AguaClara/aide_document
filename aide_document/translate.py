# -*- coding: utf-8 -*-

import yaml
from googletrans import Translator

def replace(dict,line):
    """
    Find and replace the special words according to the dictionary.

    Parameters
    ==========
    dict : Dictionary
        A dictionary derived from a yaml file. Source language as keys and the target language as values.
    line : String
        A string need to be processed.
    """
    words = line.split()
    new_line = ""

    for word in words:
        fst = word[0]
        last = word[-1]
        # Check if the word ends with a punctuation
        if last == "," or last == ";" or last == ".":
            clean_word = word[0:-1]
            last = last + " "
        elif last == "]":
            clean_word = word[0:-1]
        else:
            clean_word = word
            last = " "

        # Check if the word starts with "["
        if fst == "[":
            clean_word = clean_word[1:]
        else:
            clean_word = clean_word
            fst = ""

        find = dict.get(clean_word)

        if find == None:
            new_line = new_line + fst + str(clean_word) + last
        else:
            new_line = new_line + fst + str(find) + last
            
    return new_line

def translate(src_filename, dest_filename, dest_lang, src_lang='auto', specialwords_filename=''):
    """
    Converts a source file to a destination file in the selected language.

    Parameters
    ==========
    src_filename : String
        Relative file path to the original MarkDown source file.
    dest_filename : String
        Relative file path to where the translated MarkDown file should go.
    dest_lang : String
        The language of the destination file. Must be the correct 2-letter ISO-639-1 abbreviation from https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
    src_lang : String (OPTIONAL)
        The language of the source file. Only needed if the source file contains multiple languages. Like dest_lang, must be the correct ISO-639-1 abbreviation from https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
    specialwords_filename : String (OPTIONAL)
        YAML file containing special translations of words. Must map a string of the translation direction (e.g. 'en_es') to a sequence of specially translated words.

    Examples
    ========
    Suppose you have the following directory in English:
    data/
        doc_en.md
        special.yaml

    special.yaml is organized as follows:
    en_es:
      - tank : bote #TODO: add more/better translation examples

    To translate it to Spanish:
    >>> from aide_document import translate
    >>> translate.translate('data/doc_en.md', 'data/doc_es.md', 'es', 'en', 'data/special.yaml')

    The 4th parameter can be omitted if the source file has only one language, and the 5th can be omitted if there are no special translations.
    """
    translator = Translator() # Initialize translator object

    with open(src_filename) as srcfile, open(dest_filename, 'w') as destfile:

        lines = srcfile.readlines()
        specialwords_dict = {}

        # If special words file exists, place special word mappings into specialwords_dict
        if specialwords_filename != '':
            with yaml.load(open(specialwords_filename)) as specialwords_fulllist:

                # Gets source language if not passed through
                if src_lang == 'auto':
                    src_lang == str(translator.detect(lines[0]))[14:16]

                # Attempts to add the correct dictionary of special words
                try:
                    specialwords_dict = specialwords_dict_full[src_lang + '_' + dest_lang]
                except KeyError:
                    print('Special words file doesn\'t contain required language translation!')

        # Parses each line for special cases and ignores them when translating
        for line in lines:
            line = line.strip()

            # Parses for code blocks and ignores them entirely
            if line.startswith("```"):
                line = line

            else:
                # Parses for URL's and file links and ignores them
                if line.find("[") != -1 and line.find("]") != -1 and line.find("(") != -1 and line.find(")") != -1:
                    ignore_start = line.find("(")
                    ignore_end = line.find(")")
                    head = replace(specialwords_dict,line[0:ignore_start])
                    tail = replace(specialwords_dict,line[ignore_end+1:])
                    head = translator.translate(head, dest_lang, src_lang).text
                    tail = translator.translate(tail, dest_lang, src_lang).text
                    line = head + line[ignore_start:ignore_end+1] + tail

                # Translates normally if there are no special cases
                else:
                    line = translator.translate(line, dest_lang, src_lang).text

            # Write to destination file
            destfile.write(line + '\n')
