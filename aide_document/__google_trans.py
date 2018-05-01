from googletrans import Translator

translator = Translator()

def api(input, src_lan, tar_lan):
    """
    Return the string result from the googletrans translation.
    It is a sentence-level translation.

    Parameters
    ==========
    [input] : string
    The sentence needs to be translated.
    [src_lan] : string
    The language of the input file content. Must be the correct abbreviation.
    [tar_lan] : string
    The language of the output file content. Must be the correct abbreviation.
    """
    result = translator.translate(input, src = src_lan, dest = tar_lan )
    return result.text
