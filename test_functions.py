import unittest
from io import StringIO
from unittest.mock import patch
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
        with captured_io("") as (out, err): # handles output stream and redirects back into programme rather that console
            basic_correctness_check = mastermind.check_correctness(1, 4)
            prompt_user_again_check1 = mastermind.check_correctness(1, 0)
            prompt_user_again_check2 = mastermind.check_correctness(1, 1)
            prompt_user_again_check3 = mastermind.check_correctness(1, 2)
            prompt_user_again_check4 = mastermind.check_correctness(1, 3)


        self.assertTrue(basic_correctness_check)
        self.assertFalse(prompt_user_again_check1)
        self.assertFalse(prompt_user_again_check2)
        self.assertFalse(prompt_user_again_check3)
        self.assertFalse(prompt_user_again_check4)

    
    #@patch("sys.stdin", StringIO("123\n12\n1234\n"))
    def test_get_user_input(self):
        
        #self.assertEqual(mastermind.get_answer_input(), "1234")

        with captured_io(StringIO("123\n12\n1234")) as (out, err):
            response = mastermind.get_answer_input()
            output = out.getvalue().strip()

        self.assertEqual("Input 4 digit code: Please enter exactly 4 digits.\nInput 4 digit code: Please enter exactly 4 digits.\nInput 4 digit code:", output)
        self.assertTrue("1234", response) #checks that only "1234" is returned from function as other inputs are invalid


    def test_take_turn(self):
        with captured_io("") as (out, err):
            response = mastermind.take_turn("1234", [1, 2, 3, 4])
            output = out.getvalue().strip()

        self.assertEqual("Number of correct digits in correct place:     4\nNumber of correct digits not in correct place: 0", output)
        self.assertTrue([4, 0], response)