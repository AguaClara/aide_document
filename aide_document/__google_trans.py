"""
Auxiliary function for translate.py.
DOCUMENTATION NEEDED
"""

from googletrans import Translator

translator = Translator()

def api(input, src_lan, tar_lan):
    result = translator.translate(input, src = src_lan, dest = tar_lan )
    return result.text