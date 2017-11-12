###add testing

import unittest
import io
from aide_document.json_to_latex import json_to_latex_header

class TestJson2Latex(unittest.TestCase):
    """
    Test aide_document's json_to_latex file
    """

    def test_1(self):
       data_file = 'aide_document/json/test2.json' 
       header_file = 'aide_document/latex/test1.tex'
       header_file_check = 'aide_document/latex/test1_check.tex'
        
       json_to_latex_header(data_file, header_file)

       f1 = open(header_file, 'r')
       f2 = open(header_file_check, 'r')

       assertEqual(f1.read(), f2.read())
