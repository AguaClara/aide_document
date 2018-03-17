# -*- coding: utf-8 -*-
from googletrans import Translator
translator = Translator()
def trans(input, src_lan, tar_lan):
    result = translator.translate(input, src = src_lan, dest = tar_lan )
    return result.text
