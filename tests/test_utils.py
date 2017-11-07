"""
aide_document tests.
"""

import unittest
import io
from aide_document.utils import read_json


class TestUtils(unittest.TestCase):
    """
    Test aide_document's utils.
    """

    def setUp(self):
        self.test1 = 'aide_document/json/test1.json'

    def test_read_json_no_units(self):
        try:
            in_file = open(self.test1,'r')    
        except IOError:
            self.assertEqual(1,0, "can't find test1.json")
            return
        
        json_string = in_file.read()
        in_file.close()
        out = read_json("test_key_1",json_string)
        self.assertEqual(out, "5")

    def test_read_json_w_units(self):
        try:
            in_file = open(self.test1,"r")
        except IOError:
            self.assertEqual(1,0, "can't find test1.json")
            return

        json_string = in_file.read()
        in_file.close()
        out = read_json("test_key_2", json_string)
        self.assertEqual(out, "10.00 mg/L")

if __name__ == '__main__':
    unittest.main()
