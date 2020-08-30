import unittest
from io import StringIO
import sys
from test_base import captured_io
from test_base import run_unittests
import mastermind

class TestMastermind(unittest.TestCase):

    def test_create_code(self):
        code_is_valid = False

        for i in range (2):
            code = mastermind.create_code()
            is_valid_list = [element for element in code if str(element).isdigit() and element >= 1 and element <= 8]
            if len(code) == 4 and len(code) == len(is_valid_list) and len(code) == len(set(code)):
                #print(code) 
                code_is_valid = True
                  
        
        self.assertTrue(code_is_valid, "code should contain 4 digits in range 1-8, no duplicates.")