import unittest
from new_cal import add
from new_cal import subtract


class AddTestCase(unittest.TestCase):
    def test_add(self):
        result = add(2, 3)
        self.assertEqual(result, 5, "Incorrect sum")
    def test_sub(self):
        r=subtract(3,6)
        self.assertEqual(r,-3,"incorrect ")
         

if __name__ == '__main__':
    unittest.main()
