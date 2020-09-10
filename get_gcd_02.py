def get_gcd(m,n):
    """
    Function to get the greatest common divisor of number using Euclid Algo (Recursive Approach).
    Input m & n numbers
    >>> import get_gcd_02 as gcd
    >>> print(gcd.get_gcd(48,18))
    6
    """
    if m==0 and n==0:
        return None
    elif m==0:
        return n
    elif n==0:
        return m
    elif m is None or n is None:
        return 'Item cannot be None'
    else:
        # m>n check
        if m<n:
            m,n = n,m

        if m%n==0:
            return n
        else:
            return (get_gcd(n,m%n))

import unittest
class TestGCD(unittest.TestCase):

    def test1(self):
        self.assertEqual(get_gcd(None,None), "Item cannot be None", "Should be None")
        self.assertEqual(get_gcd(0,0), None, "Should be None")
        self.assertEqual(get_gcd(0,10), 10, "Should be 10")
        self.assertEqual(get_gcd(11,0), 11, "Should be 11")

    def test2(self):
        self.assertEqual(get_gcd(48,18), 6, "Should be 6")
        self.assertEqual(get_gcd(18,19), 1, "Should be 1")
        self.assertEqual(get_gcd(18,28), 2, "Should be 2")
        self.assertEqual(get_gcd(98,56), 14, "Should be 14")
        self.assertEqual(get_gcd(48,18), 6, "Should be 6")


if __name__ == "__main__":
    unittest.main()