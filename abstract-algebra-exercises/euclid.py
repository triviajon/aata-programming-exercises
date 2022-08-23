# 2.4.3

"""
Write a computer program that will implement the Euclidean algorithm. The program
should accept two positive integers a and b as input and should output gcd(a, b) as well as
integers r and s such that
gcd(a, b) = ra + sb
"""

def ExtendedEuclidAlgorithm(a, b):
    assert isinstance(a, int) and isinstance(b, int), ValueError("a and b must be of type int")
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t

    return old_r, old_s, old_t