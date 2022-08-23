# 16.7.1
"""
Write a computer program implementing fast addition and multiplication using the
Chinese Remainder Theorem. 

Chinese Remainder Theorem. Let N = {n1, n2, . . . , nk} be positive integers such
that gcd(ni, nj) = 1 for i ̸= j.

Then for any integers A = {a1, . . . , ak}, the system
x ≡ a1 (mod n1)
x ≡ a2 (mod n2)
...
x ≡ ak (mod nk)
has a solution that is unique (mod n1*n2*...*nk).

Idea:
x ≡ a1 (mod n1)
x ≡ a2 (mod n2)
has a solution (mod n1*n2). This is given by
x = a1 + k*n1 where 
k = (a2-a1)*s and s is the integer so that
n1*s + n2*t = 1.

So the idea for the algorithm is as follows:
Inputs: x, y
Outputs: x*y

1. Find integers N = {n1, n2, .., nk} s.t. gcd(ni, nj) = 1 and prod(n_i) > x*y.
2. Breakdown x (mod ni) and y (mod ni) for every ni. 
3. Multiply x*y (mod ni) for every ni. (or addition)
4. Solve the congruences x*y (mod ni). (or addition)
"""
# Step 4 requires using the extended euclidean algorithm
from euclid import ExtendedEuclidAlgorithm

def prod(L):
    return L[0] if len(L) == 1 else prod(L[1:])*L[0]

# Step 4 of the algorithm is solving systems of congruences
def solve_congruence(A, N):
    """
    Solves systems of conguences of the form:
    x ≡ a1 (mod n1)
    x ≡ a2 (mod n2)
    ...
    x ≡ ak (mod nk)
    Recursive for now...
    """
    assert (len(A) == len(N)) and (len(A) > 1), ValueError("Must have more than 1 system.")
    k = len(A)

    if isinstance(A, (tuple, set)): A = list(A)
    if isinstance(N, (tuple, set)): N = list(N)

    if k == 2:
        pairgcd, s, t = ExtendedEuclidAlgorithm(N[0], N[1])
        return (A[0] + (A[1]-A[0])*s*N[0])%(N[0]*N[1])
    else: 
        A1, A2 = A[0:2], A[2:k]
        N1, N2 = N[0:2], N[2:k]
        newa, newn = solve_congruence(A1, N1), prod(N1)
        return solve_congruence([newa,] + A2, [newn,] + N2)

# Step 1 requires finding pairwise coprime integers
def coprimes(geq, N):
    """
    Finds N pairwise coprime integers whose product is at least as large as geq.
    """
    def is_prime(n):
        return not any([n%j==0 for j in range(2, 1+int(n**(1/2)))])

    # genetate primes greater than or equal to geq
    primes = [2, ]
    prime_prod = prod(primes)
    i = 3

    while prime_prod < geq: 
        if is_prime(i):
            primes.append(i)
            prime_prod *= i
        i += 1
    
    res = [1 for i in range(N)]
    for i in range(0, len(primes), N):
        for k in range(len(res)):
            factor = primes[i+k] if len(primes) > i+k else 1
            res[k] *= factor
    return res

# Algorithms
def fast_add(x, y, k=4):
    # Step 1: Find integers N = {n1, n2, .., nk} s.t. gcd(ni, nj) = 1 and prod(n_i) > x*y.
    # Note that 10^(order(x)+order(y)) > x*y

    xord, yord = len(str(x)), len(str(y))
    N = coprimes(10**(xord+yord), k)
 
    # Step 2: Breakdown x (mod ni) and y (mod ni) for every ni. 
    # Step 3: Add x+y (mod ni) for every ni.
    A = [((x%ni)+(y%ni))%ni for ni in N]

    # Step 4: Solve the congruences x+y (mod ni).
    soln = solve_congruence(A, N)
    return soln

def fast_mult(x, y, k=4):
    # Step 1: Find integers N = {n1, n2, .., nk} s.t. gcd(ni, nj) = 1 and prod(n_i) > x*y.
    # Note that 10^(order(x)+order(y)) > x*y

    xord, yord = len(str(x)), len(str(y))
    N = coprimes(10**(xord+yord), k)
 
    # Step 2: Breakdown x (mod ni) and y (mod ni) for every ni. 
    # Step 3: Add x+y (mod ni) for every ni.
    A = [((x%ni)*(y%ni))%ni for ni in N]

    # Step 4: Solve the congruences x+y (mod ni).
    soln = solve_congruence(A, N)
    return soln

if __name__ == "__main__":
    #print(solve_congruence((9, 0, 30, 55), (95, 97, 98, 99)))
    print(fast_mult(832430, 4893243))