class SimpleDistortedInt:
    """
    Wrapper for an integer value that supports the rule x ⊗ y = 2x − y.
    """
    def __init__(self, obj):
        """
        Sets the wrapped value to that of the passed parameter.
        """
        self.object = obj

    def __str__(self):
        """
        Returns a useful string representation.
        """
        return "<"+str(self.object)+">"

    def __mul__(self, other):
        """
        Defines the operation of the '*' operator as x ⊗ y = 2x − y.
        """
        return SimpleDistortedInt(2 * self.object - other.object)


class DistortedError(Exception):

    # Not yet implemented, but this is the basic idea
    def __init__(self, dint1, dint2):
        self.dint1 = dint1
        self.dint2 = dint2
        self.message = "Cannot perform operation."
        # should add a better explanation of why


# Basic Requirements 
class DistortedInt:
    """
    Discrete mathematical structures defined as a value (x), modulus (n) and distortion (alpha).
    Support a binary operation, which we call multiplication, given by the rule x ⊗ y = (alpha x + (1 − alpha) y) mod n where:
        - n is a fixed positive integer
        - alpha is a fixed element of the set {0, 1, ..., n-1}, denoted Zn
        - x and y are taken from the set Zn 
        - the result is reduced modulo n to ensure that it belongs to Zn
        - x ⊗ y can be calculated iff x and y are defined for the same modulus and distortion
    """

    def __init__(self, val, mod, dis):
        """
        Initialises a member of the class such that the x = val, n = mod, alpha = dis.
        """
        if val >= mod or dis >= mod:
            raise Exception("Value and distortion must be in the set {0, 1, ..., n-1} where n is the modulus.")
        if mod < 1 or val < 0 or dis < 0:
            raise Exception("Modulus must be greater than zero; value and distortion must be equal to or greater than zero.")
        if type(mod) != int or type(val) != int or type(dis) != int:
            raise Exception("Modulus, value and distortion must be integer values.")
        self.value = val
        self.modulus = mod
        self.distortion = dis

    def __str__(self):
        """
        Renders a readable representation of a distorted integer.
        """
        return "<" + str(self.value) + " mod " + \
            str(self.modulus) + " | " + \
            str(self.distortion) + " >"

    def __mul__(self, other):
        """
        Defines the operation of the '*' operator as per the rule in the class's definition.
        """
        if self.distortion != other.distortion or self.modulus != other.modulus:
            raise Exception(
                "Modulus and distortion of both arguments must match.")
        else:
            a = self.distortion
            n = self.modulus
            x = self.value
            y = other.value
            result = (a * x + (1 - a) * y) % n
            return DistortedInt(result, n, a)

    # define "=="
    def __eq__(self, other):
        """
        Defines equality between distorted integers as dependent upon the equality of the values, moduli and alphas of the two distorted integers.
        """
        equal = True
        if self.value != other.value:
            equal = False
        if self.modulus != other.modulus:
            equal = False
        if self.distortion != other.distortion:
            equal = False
        return equal


# Medium 1
class DistortedIntegers:
    """
    An abstraction representing the set Zn.
    """
    def __init__(self, n, alpha):
        """
        Initilises to hold the values of modulus and distortion.
        """
        if alpha >= n:
            raise Exception(
                "Distortion must be in the set {0, 1, ..., n-1} where n is the modulus.")
        if n < 1 or alpha < 0:
            raise Exception(
                "Modulus must be greater than zero; distortion must be equal to or greater than zero.")
        if type(n) != int or type(alpha) != int:
            raise Exception(
                "Modulus and distortion must be integer values.")
        self.modulus = n
        self.distortion = alpha

    def generate(self, x):
        """
        Generates distorted integers to represent the set Zn for the object's defined modulus and distortion.
        """
        while x < self.modulus:
            yield DistortedInt(x, self.modulus, self.distortion)
            x += 1

    def __str__(self):
        """
        Utilises the generator to create a string representing the distorted integers for the complete set Zn.
        """
        string = ""
        for i in self.generate(0):
            string += str(i) + "\n"
        return string

    def size(self):
        """
        There can be a number of distorted integers equal to the magnitude of the modulus so this value is returned.
        """
        return self.modulus


# Medium 2
class IteratorOfDistortedInteger:
    """
    Simple iterator to allow for iteration over an instance of the DistortedIntegers class.
    """
    def __init__(self, dis_ints):
        self.dis_ints = dis_ints
        self.max = self.dis_ints.size()
        self.index = 0
        self.list = []
        for i in self.dis_ints.generate(0):
            self.list.append(i)

    def __iter__(self):
        return self

    def __next__(self):
        """
        Increments the index counter and returns the corresponding item until it is detected that the end of the set has been reached.
        """
        if self.index == self.max:
            raise StopIteration
        self.index = self.index + 1
        return self.list[self.index - 1]
