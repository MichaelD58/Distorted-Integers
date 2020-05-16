import unittest
from distortedint import DistortedInt, DistortedIntegers


class BasicReqTestCases(unittest.TestCase):

    # Test basic construction

    def test_construction(self):
        self.dint = DistortedInt(1, 3, 2)
        self.assertIsNotNone(self.dint)

    def test_to_string(self):
        self.dint = DistortedInt(1, 3, 2)
        self.assertEqual(str(self.dint), "<1 mod 3 | 2 >")

    # Test exceeding modulus

    def test_x_exceeds_n(self):
        with self.assertRaises(Exception):
            DistortedInt(10, 5, 3)

    def test_a_exceeds_n(self):
        with self.assertRaises(Exception):
            DistortedInt(3, 5, 10)

    def test_x_a_exceed_n(self):
        with self.assertRaises(Exception):
            DistortedInt(10, 5, 15)

    # Test not positive integers

    def test_n_negative(self):
        with self.assertRaises(Exception):
            DistortedInt(-6, -5, -6)

    def test_x_negative(self):
        with self.assertRaises(Exception):
            DistortedInt(-6, 10, 6)

    def test_a_negative(self):
        with self.assertRaises(Exception):
            DistortedInt(6, 10, -6)

    def test_n_non_integer(self):
        with self.assertRaises(Exception):
            DistortedInt(3, 7.5, 5)

    def test_x_non_integer(self):
        with self.assertRaises(Exception):
            DistortedInt(3.4, 7, 5)

    def test_a_non_integer(self):
        with self.assertRaises(Exception):
            DistortedInt(3, 7, 5.6)

    # Test 'multiplication'

    def test_success(self):
        x = DistortedInt(2, 5, 3)
        y = DistortedInt(4, 5, 3)
        result = DistortedInt(3, 5, 3)
        self.assertEqual(x * y, result)

    def test_mismatch_n(self):
        x = DistortedInt(4, 5, 3)
        y = DistortedInt(2, 6, 3)
        with self.assertRaises(Exception):
            x * y

    def test_mismatch_a(self):
        x = DistortedInt(4, 5, 3)
        y = DistortedInt(2, 5, 2)
        with self.assertRaises(Exception):
            x * y

    def test_mismatch_n_a(self):
        x = DistortedInt(4, 5, 3)
        y = DistortedInt(2, 6, 4)
        with self.assertRaises(Exception):
            x * y

    def test_a_zero(self):
        x = DistortedInt(2, 7, 0)
        y = DistortedInt(5, 7, 0)
        # when a == 0, result == y
        self.assertEqual(x * y, y)

    def test_a_one(self):
        x = DistortedInt(2, 7, 1)
        y = DistortedInt(5, 7, 1)
        # when a == 1, result == x
        self.assertEqual(x * y, x)

    # The above two tests effectively test both cases of n = 1

    def test_x_not_equal(self):
        x = DistortedInt(2, 7, 1)
        y = DistortedInt(5, 7, 1)
        self.assertFalse(x == y)
   
    def test_n_not_equal(self):
        x = DistortedInt(2, 7, 1)
        y = DistortedInt(2, 8, 1)
        self.assertFalse(x == y)

    def test_a_not_equal(self):
        x = DistortedInt(2, 7, 1)
        y = DistortedInt(2, 7, 2)
        self.assertFalse(x == y)


class Medium3TestCases(unittest.TestCase):
    # Test exceeding modulus

    def test_a_exceeds_n(self):
        with self.assertRaises(Exception):
            DistortedIntegers(5, 10)

    # Test not positive integers

    def test_n_negative(self):
        with self.assertRaises(Exception):
            DistortedIntegers(-5, -6)

    def test_a_negative(self):
        with self.assertRaises(Exception):
            DistortedIntegers(10, -6)

    def test_n_non_integer(self):
        with self.assertRaises(Exception):
            DistortedIntegers(7.5, 5)

    def test_a_non_integer(self):
        with self.assertRaises(Exception):
            DistortedIntegers(7, 5.6)

    def test_to_string(self):
        xs = DistortedIntegers(3,2)
        self.assertEqual(str(xs), "<0 mod 3 | 2 >\n<1 mod 3 | 2 >\n<2 mod 3 | 2 >\n")


if __name__ == '__main__':
    unittest.main()
