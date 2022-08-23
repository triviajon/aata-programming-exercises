# 4.5.2
"""
Write a computer program to calculate a^x (mod n) by the method of repeated squares.
What are the largest values of n and x that your program will accept?

Idea:
Suppose we need to calculate a^x (mod n).
We can take x's binary representation to write it as a sum of powers of 2:
x = 2^i0 + 2^i1 + ...
so a^x = a^(2^i0 + 2^i1 + ...) = a^(2^(i0)) * a^(2^(i1)) * ... (mod n)

And so we can compute a^(2^(ij)) (mod n)...
"""