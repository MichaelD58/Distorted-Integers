import unittest

from distortedint_functions import HasDistortedIdempotentProperty, HasDistortedIdempotentPropertyIterator, \
    DistortedRootsOfOne, DistortedRootsOfOneIterator, IsCommutativeDistortedMultiplication, IsCommutativeDistortedMultiplicationIterator, \
    IsAssociativeDistortedMultiplication, IsAssociativeDistortedMultiplicationIterator, IsQuasiDistributiveDistortedMultiplication, \
    IsQuasiDistributiveDistortedMultiplicationIterator, HasDistortedEquationProperty
from distortedint import DistortedInt



class FunctionTestCases(unittest.TestCase):

    # Easy 1

    def test_distorted_idempotent(self):
        """
        Verifies that for each pair (n, alpha), where 1 <= n <= 100 and 0<= alpha < n, all x ∈ Zn statisfy the condition x ⊗ x = x.
        """
        for n in range(1, 101):
            for alpha in range(0, n):
                self.assertTrue(HasDistortedIdempotentProperty(n, alpha))

    # Easy 1 & Medium 2.1

    def test_distorted_idempotent_iterator(self):
        """
        Verifies that for each pair (n, alpha), where 1 <= n <= 100 and 0<= alpha < n, all x ∈ Zn statisfy the condition x ⊗ x = x, using an iterator.
        """
        for n in range(1, 101):
            for alpha in range(0, n):
                self.assertTrue(
                    HasDistortedIdempotentPropertyIterator(n, alpha))

    # Easy 2

    def test_distorted_roots_of_one(self):
        """
        Verifies that for each pair (n, alpha), where 1 <= n <= 100 and 0<= alpha < n, 
        there exists exactly one element x ∈ Zn that satisfies the condition x ⊗ x = 1.
        """
        self.assertTrue(len(DistortedRootsOfOne(1,0)) == 1)
        self.assertTrue(DistortedRootsOfOne(1,0)[0] == DistortedInt(0, 1, 0))
        # in the case of n = 1, we have Z1 = {0} and integers 0 and 1 are equivalent modulo 1
        # so it is tested outside of the main loop
        for n in range(2, 101):
            for alpha in range(0, n):
                satisfies = DistortedRootsOfOne(n, alpha)
                self.assertTrue(len(satisfies) == 1)
                self.assertTrue(satisfies[0] == DistortedInt(1, n, alpha))

    # Easy 2 & Medium 2.2

    def test_distorted_roots_of_one_iterator(self):
        """
        Verifies that for each pair (n, alpha), where 1 <= n <= 100 and 0<= alpha < n, 
        there exists exactly one element x ∈ Zn that satisfies the condition x ⊗ x = 1, using an iterator.
        """
        self.assertTrue(len(DistortedRootsOfOneIterator(1,0)) == 1)
        self.assertTrue(DistortedRootsOfOneIterator(1,0)[0] == DistortedInt(0, 1, 0))
        # in the case of n = 1, we have Z1 = {0} and integers 0 and 1 are equivalent modulo 1
        # so it is tested outside of the main loop
        for n in range(2, 101):
            for alpha in range(0, n):
                satisfies = DistortedRootsOfOneIterator(n, alpha)
                self.assertTrue(len(satisfies) == 1)
                self.assertTrue(satisfies[0] == DistortedInt(1, n, alpha))

    # Easy 3
    def test_commutative_distorted_multiplication(self):
        """
        Demonstrates with two examples that IsCommutativeDistortedMultiplication() renders correct results.
        Holds true for X = 5, Y = 3, n = 7, alpha = 4 such that x = <X mod n | alpha >
        False for all X and Y where n = 20, alpha = 11 such that x = <X mod n | alpha >
        """
        self.assertTrue(IsCommutativeDistortedMultiplication(7, 4))
        self.assertFalse(IsCommutativeDistortedMultiplication(21, 10))

    # Easy 3 & Medium 2.3
    def test_commutative_distorted_multiplication_iterator(self):
        """
        Demonstrates with two examples that IsCommutativeDistortedMultiplicationIterator() renders correct results, using an iterator.
        Holds true for X = 5, Y = 3, n = 7, alpha = 4 such that x = <X mod n | alpha >
        False for all X and Y where n = 20, alpha = 11 such that x = <X mod n | alpha >
        """
        self.assertTrue(IsCommutativeDistortedMultiplicationIterator(7, 4))
        self.assertFalse(IsCommutativeDistortedMultiplicationIterator(21, 10))

    # Easy 4
    def test_associative_distorted_multiplication(self):
        """
        Demonstrates with two examples that IsAssosicativeDistortedMultiplication() renders correct results.
        Holds true for X = 5, Y = 3, Z = 1, n = 6, alpha = 3 such that x = <X mod n | alpha >
        False for all X, Y, Z where n = 3, alpha = 2 such that x = <X mod n | alpha >
        """
        self.assertTrue(IsAssociativeDistortedMultiplication(6, 3))
        self.assertFalse(IsAssociativeDistortedMultiplication(3, 2))

    # Easy 4 & Medium 2.4
    def test_associative_distorted_multiplication_iterator(self):
        """
        Demonstrates with two examples that IsAssosicativeDistortedMultiplicationIterator() renders correct results.
        Holds true for X = 5, Y = 3, Z = 1, n = 6, alpha = 3 such that x = <X mod n | alpha >
        False for all X, Y, Z where n = 3, alpha = 2 such that x = <X mod n | alpha >
        """
        self.assertTrue(IsAssociativeDistortedMultiplicationIterator(6, 3))
        self.assertFalse(IsAssociativeDistortedMultiplicationIterator(3, 2))

    # Easy 5
    def test_quasi_distorted_multiplication(self):
        """
        Demonstrates with two examples that IsQuasiDistributiveDistortedMultiplication() renders correct results.
        Holds true for X, Y , Z, where n = 6, alpha = 4 such that x = <X mod n | alpha >
        False for all X = 1, Y = 3, Z = 3, n = 6, alpha = 5 such that x = <X mod n | alpha >
        """
        self.assertTrue(IsQuasiDistributiveDistortedMultiplication(6, 4))
        self.assertFalse(IsQuasiDistributiveDistortedMultiplication(6, 5))

    # Easy 5 & Medium 2.5
    def test_quasi_distorted_multiplication_iterator(self):
        """
        Demonstrates with two examples that IsQuasiDistributiveDistortedMultiplicationIterator() renders correct results.
        Holds true for X, Y , Z, where n = 6, alpha = 4 such that x = <X mod n | alpha >
        False for all X = 1, Y = 3, Z = 3, n = 6, alpha = 5 such that x = <X mod n | alpha >
        """
        self.assertTrue(IsQuasiDistributiveDistortedMultiplicationIterator(6, 4))
        self.assertFalse(IsQuasiDistributiveDistortedMultiplicationIterator(6, 5))

    # Medium 3
    def test_distorted_equation(self):
        """
        Demonstrates with three examples that HasDistortedEquationProperty() renders correct results.
        There are multiple values of y that satisfy x*y=z for z, x = <0 mod 4 | 1 > so the property doesn't hold
        There are no values of y that satisfy the above for  x = <5 mod 6 | 5 >, z = <4 mod 6 | 5 > so the property doesn't hold
        There is a unique value of y that satisfies the above for x, z = <0 mod 6 | 2 > so the property does hold.
        """
        self.assertFalse(HasDistortedEquationProperty(4, 1))
        self.assertFalse(HasDistortedEquationProperty(6, 5))
        self.assertTrue(HasDistortedEquationProperty(6, 2))


if __name__ == '__main__':
    unittest.main()
