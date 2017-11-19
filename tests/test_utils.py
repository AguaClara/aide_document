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
        self.test1 = 'tests/test_json_files/test1.json'

    def test_read_json_no_units(self):
        try:
            in_file = open(self.test1,'r')    
        except IOError:
            self.assertEqual(1,0, "can't find test1.json")
            return
        
        json_string = in_file.read()
        in_file.close()
        out = read_json("test_key_1",json_string)
        self.assertEqual(out, '5')

        #Value should not have type string
        with self.assertRaises(TypeError):
          read_json("test_key_3",json_string)

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

        #Unimplemented currently. Should not make a difference if there is an extra unused variable in the json
        out2 = read_json("test_key_4", json_string)
        self.assertEqual(out2, "10.00 mg/L")

        #Should not have a string associated with the Value field
        with self.assertRaises(TypeError):
          read_json("test_key_5", json_string)
if __name__ == '__main__':
    unittest.main()
