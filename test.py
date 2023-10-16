import unittest
from multipli import multipication

class TestMultipication(unittest.TestCase):
    def test_multiply1(self):

        # Create an instance of the multipication class
        calculator = multipication()

        # Perform the assertion
        self.assertEqual(calculator.multiply1(1, 1), 2)
    
    def test_multiply2(self):
        # Create an instance of the multipication class
        calculator = multipication()

        # Perform the assertion
        
        self.assertEqual(calculator.multiply2(1, 1),1)

if __name__ == '__main__':
    unittest.main()
