import unittest
from src.math import Math

class TestMathClass(unittest.TestCase):

    def  test_addition(self):
        self.assertEqual(Math.addition(2,3),5,"Must be 5")

    def test_divide(self):
        self.assertEqual(Math.divide(1,2),1/2,'Must be 1/2')     