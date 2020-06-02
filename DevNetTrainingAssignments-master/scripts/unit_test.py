import unittest
import check

class TestMyFunctions(unittest.TestCase):
    def test(self):
        self.assertEqual(check.fun(3), 4)
unittest.main() 
