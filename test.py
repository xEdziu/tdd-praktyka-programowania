from calculator import * # plik z kalkulatorem calculator.py
import unittest

class TestAdd(unittest.TestCase):

    def test_empty_string(self):
        for i in range(10):
            self.assertEqual(Add(""),0)

    def test_one_digit(self):
        for i in range(10):
            self.assertEqual(Add(f"{i}"),i)

    def test_two_digits(self):
        for i in range(10):
            self.assertEqual(Add(f"{i},{i+1}"),i+i+1)

    def test_multiple_digits(self):
        for i in range(10):
            self.assertEqual(Add(f"{i},{i+1},{i+2}"),i+i+1+i+2)

    def test_no_number(self):
        for i in range(10):
            with self.assertRaises(ValueError):
                Add(",")

    def test_different_devider(self):
        for i in range(10):
            self.assertEqual(Add(f"{i}\n{i+1}\n{i+2}"),i+i+1+i+2)
            self.assertEqual(Add(f"{i}\n{i+3},{i+4}"),i+i+3+i+4)
    
    def test_incorrect_argument(self):
        for i in range(10):
            with self.assertRaises(ValueError):
                Add(f"{i}\n,{i+1}")
            with self.assertRaises(ValueError):
                Add(f"{i}\n,")
            with self.assertRaises(ValueError):
                Add(f",\n{i}")
            with self.assertRaises(ValueError):
                Add(f"{i}\n\n{i}")
            with self.assertRaises(ValueError):
                Add(f"{i},,")




