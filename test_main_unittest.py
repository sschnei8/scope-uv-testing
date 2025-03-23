import unittest
from main import main

class TestMain(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(main(1, 2, 3), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main() 