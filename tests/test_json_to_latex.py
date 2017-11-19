###add testing

import unittest
import io
import os.path
from aide_document.json_to_latex import json_to_latex_header

class TestJson2Latex(unittest.TestCase):
    """
    Test aide_document's json_to_latex file
    """

    def test_1(self):
     
       data_file = 'tests/test_json_files/test2.json' 
       header_file = 'tests/test_latex_files/test1.tex'

       
       if(os.path.isfile(header_file)):
            f = open(header_file, 'w') 
            f.write("")
            f.close()

       header_file_check = 'tests/test_latex_files/test1_check.tex'
        
       json_to_latex_header(data_file, header_file)

       f1 = open(header_file, 'r')
       f2 = open(header_file_check, 'r')

       self.assertEqual(f1.read(), f2.read())
