from distortedint import DistortedInt, DistortedIntegers, IteratorOfDistortedInteger


# Convenience, can use for all the boolean functions
def GetPairs(f, upper):
    """
    Pass a function that returns a boolean and an upper bound to collect pairs of (n, alpha) that satisfy a
    condition as specified by the function f.
    """
    pairs = []
    for n in range(1, upper + 1):
        for alpha in range(0, n):
            if f(n, alpha):
                pairs.append((n, alpha))
    return pairs


# Easy 1
def HasDistortedIdempotentProperty(n, alpha):
    """
    Checking all values between 0 and n to see if the result of distortedint returns True for values of x in the
    set for x*x = x.
    """
    for i in range(0, n):
        x = DistortedInt(i, n, alpha)
        if x * x != x:
            return False
    return True


# Easy 2
def DistortedRootsOfOne(n, alpha):
    """
    Returns a list containing all the distortedint values for all elements of x in the set that satisfies the
    condition x*x = 1.
    """
    if (n == 1):
        return [DistortedInt(0, n, 0)]
        # 1 modulo 1 and 0 modulo 1 are equivalent, so in the exceptional case that n == 1
        # x ⊗ x = 1 is equivalent to x ⊗ x = 0, which is always true for the only possible value of x and alpha which is 0
        # therefore, we can return a list of length 1 containing DistortedInt(0,1,0)
    roots = []
    for i in range(0, n):
        x = DistortedInt(i, n, alpha)
        if x * x == DistortedInt(1, n, alpha):
            roots.append(x)    
    return roots


# Easy 3
def IsCommutativeDistortedMultiplication(n, alpha):
    """
    Checking to see if, given n and alpha, all values for x and y in the set hold True for the function x*y = y*x.
    """
    for i in range(0, n):
        x = DistortedInt(i, n, alpha)
        for j in range(0, n):
            y = DistortedInt(j, n, alpha)
            if (x * y) != (y * x) or (n % 2 == 0):  # Verifying that all n are odd
                return False
    return True


# Easy 4
def IsAssociativeDistortedMultiplication(n, alpha):
    """
    Checking to see if, given n and alpha, all values for x, y and z in the set hold True for the function (x*y)*z
    = x*(y*z).
    """
    for a in range(0, n):
        x = DistortedInt(a, n, alpha)
        for b in range(0, n):
            y = DistortedInt(b, n, alpha)
            for c in range(0, n):
                z = DistortedInt(c, n, alpha)
                if (x * y) * z != x * (y * z):
                    return False
    return True


# Easy 5
def IsQuasiDistributiveDistortedMultiplication(n, alpha):
    """
    Checking to see if, given n and alpha, all values for x, y and z in the set hold True for the function (x*y)*z
    = (x*y)*(x*z).
    """
    for a in range(0, n):
        x = DistortedInt(a, n, alpha)
        for b in range(0, n):
            y = DistortedInt(b, n, alpha)
            for c in range(0, n):
                z = DistortedInt(c, n, alpha)
                if (x * y) * z != (x * y) * (x * z):
                    return False
    return True


# Medium 2
    # Medium 2.1
def HasDistortedIdempotentPropertyIterator(n, alpha):
    """
    Checking all values between 0 and n using an iterator to see if the result of distortedint returns True for
    values of x in the set for x*x = x.
    """
    for x in IteratorOfDistortedInteger(DistortedIntegers(n, alpha)):
        if x * x != x:
            return False
    return True

    # Medium 2.2
def DistortedRootsOfOneIterator(n, alpha):
    """
    Returns a list containing all the distortedint values for all elements of x in the set that satisfies the
    condition x*x = 1 using an iterator.
    """
    if (n == 1):
        return [DistortedInt(0, n, 0)]
        # 1 modulo 1 and 0 modulo 1 are equivalent, so in the exceptional case that n == 1
        # x ⊗ x = 1 is equivalent to x ⊗ x = 0, which is always true for the only possible value of x and alpha which is 0
        # therefore, we can return a list of length 1 containing DistortedInt(0,1,0)
    roots = []
    for x in IteratorOfDistortedInteger(DistortedIntegers(n, alpha)):
        if x * x == DistortedInt(1, n, alpha):
            roots.append(x)
    return roots

    # Medium 2.3
def IsCommutativeDistortedMultiplicationIterator(n, alpha):
    """
    Checking to see if, given n and alpha, all values for x and y in the set hold True for the function x*y = y*x
    using an iterator.
    """
    for x in IteratorOfDistortedInteger(DistortedIntegers(n, alpha)):
        for y in IteratorOfDistortedInteger(DistortedIntegers(n, alpha)):
            if (x * y) != (y * x):
                return False
    return True

    # Medium 2.4
def IsAssociativeDistortedMultiplicationIterator(n, alpha):
    """
    Checking to see if, given n and alpha, all values for x, y and z in the set hold True for the function (x*y)*z
    = x*(y*z) using an iterator.
    """
    for x in IteratorOfDistortedInteger(DistortedIntegers(n, alpha)):
        for y in IteratorOfDistortedInteger(DistortedIntegers(n, alpha)):
            for z in IteratorOfDistortedInteger(DistortedIntegers(n, alpha)):
                if (x * y) * z != x * (y * z):
                    return False
    return True

    # Medium 2.5
def IsQuasiDistributiveDistortedMultiplicationIterator(n, alpha):
    """
    Checking to see if, given n and alpha, all values for x, y and z in the set hold True for the function (x*y)*z
    = (x*y)*(x*z) using an iterator.
    """
    for x in IteratorOfDistortedInteger(DistortedIntegers(n, alpha)):
        for y in IteratorOfDistortedInteger(DistortedIntegers(n, alpha)):
            for z in IteratorOfDistortedInteger(DistortedIntegers(n, alpha)):
                if (x * y) * z != (x * y) * (x * z):
                    return False
    return True


# Medium 3
def HasDistortedEquationProperty(n, alpha):
    """
    Given a value for n and alpha, checking to see if for any x and z in the set that there is a unique y in the
    set that is True for the equation x*y=z.
    """
    for x in IteratorOfDistortedInteger(DistortedIntegers(n, alpha)):
        for z in IteratorOfDistortedInteger(DistortedIntegers(n, alpha)):
            property_holders = []
            # Checking for a "unique" y such that x*y = z...
            for y in IteratorOfDistortedInteger(DistortedIntegers(n, alpha)):
                if x * y == z:
                    property_holders.append(y)
            if len(property_holders) == 1:
                # ...so if there aren't exactly one then it is untrue
                return True
            # There being multiple x and z values that have this property \
            # doesn't seem to matter, so the function can exit here.
    return False
