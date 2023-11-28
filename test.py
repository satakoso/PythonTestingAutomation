import unittest

from main import add
from main import multiply
from main import power

class testMath(unittest.TestCase):
    
    def test_Add(self):
        """
        Test for sum function
        """
        a = 5
        b = 4
        result = add(a,b)
        self.assertEqual(result,9)
        
    def test_Multiply(self):
        """
        test for multiply function
        """
        a = 3
        b = 4
        result = multiply(a,b)
        self.assertEqual(result,12)
        
    def test_Power(self):
        """
        Test for power function
        """
        a = 2
        b = 8
        result = power(a,b)
        self.assertEqual(result,256)
        
        
        
if __name__ == '__main__':
    unittest.main()
