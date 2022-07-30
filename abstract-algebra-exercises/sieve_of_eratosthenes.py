"""

Using the Sieve of Eratosthenes,
write a program that will compute all of the primes less than an
integer N.

"""


def all_primes_to(N):
    stop = int(N**(1/2))+1
    print(stop)
    not_possible = []
    for i in range(2, stop+1):
        not_possible.extend([i*j for j in range(2, int(N/i)+1)])

    return [i for i in range(2, N) if i not in not_possible]

if __name__ == "__main__":
    pass

