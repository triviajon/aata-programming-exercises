# 4.5.1
"""
Write a computer program that will write any decimal number as the sum of distinct
powers of 2. What is the largest integer that your program will handle?

Idea:
This is just the binary representation of n. We will generalize to base k.
"""

def base_k(n, k):
    rep = ''
    while n >= 1:
        r = n%k
        n = (n-r)//k
        rep = str(r) + rep
    return rep

def binary(n):
    return base_k(n, 2)

def decimal(n):
    return base_k(n, 10)

if __name__ == "__main__":
    n, k = [int(i) for i in input("What number n would you like to convert to base k (n, k): ").split(',')]
    print(base_k(n, k))