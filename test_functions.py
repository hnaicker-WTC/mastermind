import unittest
from io import StringIO
import sys
from test_base import captured_io
from test_base import run_unittests
import mastermind

class TestMastermind(unittest.TestCase):

    def test_create_code(self):
        code_is_valid = False

        for i in range (100):
            code = mastermind.create_code()
            is_valid_list = [element for element in code if str(element).isdigit() and element >= 1 and element <= 8] #checks there are only digits in code and digits are between 1 and 8
            if len(code) == 4 and len(code) == len(is_valid_list) and len(code) == len(set(code)): # checks if code is 4 long, checks if code input is a list of 4 numbers and there are no duplicates in list
                code_is_valid = True
                  
        self.assertTrue(code_is_valid, "code should contain 4 digits in range 1-8, no duplicates.")

    
    def test_check_correctness(self):
        code_is_correct = False

        
# if __name__ == '__main__':
#     unittest.main()