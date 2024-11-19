import unittest

from prime_num import is_prime,total_sum

class TestIsPrime(unittest.TestCase):
    def test_prime_number(self):
        """testing the prime numbers"""
        self.assertTrue(is_prime(17))

    def test_non_prime_number(self):
        """testing the non prime numbers"""
        self.assertFalse(is_prime(10))


class Testsum(unittest.TestCase):
    def test_sum_equal(self):
        """testing the sum of two numbers"""
        self.assertEqual(total_sum(2,3),5)

    def test_sum_not_equal(self):
        self.assertNotEqual(total_sum(2,8),12)

if __name__ == "__main__":
    unittest.main(verbosity=2)
