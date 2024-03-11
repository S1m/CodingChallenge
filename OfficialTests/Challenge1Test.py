import unittest

from Challenge1 import Sum

class TestChallenge1(unittest.TestCase):
    def test_challenge1(self):
        c = Sum()
        self.assertEqual(c(1), 1)
        self.assertEqual(c(2), 3)
        self.assertEqual(c(3), 6)
        self.assertEqual(c(4), 10)
        self.assertEqual(c(5), 15)
        self.assertEqual(c(6), 21)
        self.assertEqual(c(7), 28)
        self.assertEqual(c(8), 36)
        self.assertEqual(c(9), 45)
        self.assertEqual(c(10), 55)

if __name__ == "__main__":
    unittest.main()