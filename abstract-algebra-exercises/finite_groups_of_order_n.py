# 13.4

"""
Write a program that will compute all possible abelian groups
of order n. What is the largest n for which your program will work?
"""

"""
Thought process:

Up to isomorphism, the fundamental theorem of finitely generated abelian groups (ft-fgag)
states that every fgag group G is isomorphic to a direct product of cyclic groups of the form:

Z_{p1^a1} x Z_{p2^a2} x ...

That being said, for any integer n, if we can find it's prime factorization:
n = p1^a1 x p2^a2 x ...

Then we can find all of the possible abelian groups of order n as such:
for any prime/power pi^ai, groups of the order pi^ai are either
Z_{pi^ai}, Z_{pi^(ai-1)} x Z_{pi}, Z_{pi^(ai-2)} x Z_{pi^2}, Z_{pi^(ai-2)} x Z_{pi} x Z_{pi}, ...

That being said, we can find all the possible abelian groups of order n by generating these 
factors and combining them.
"""

small_numbers = "₀₁₂₃₄₅₆₇₈₉"
smallify = {str(i): small_numbers[i] for i in range(10)}


class CyclicGroup:
    def __init__(self, n): 
        self.n = n
    def __repr__(self):
        return f"CyclicGroup({self.n})"
    def __str__(self):
        return "ℤ" + "".join([smallify[digit] for digit in str(self.n)])

class DirectProduct:
    def __init__(self, *groups):
        self.groups = groups
    def __repr__(self):
        return f"DirectProduct({self.groups})"
    def __str__(self):
        return " x ".join([str(g) for g in self.groups])

def prime_factorization(n, factorization={}):
    assert n >= 1 and isinstance(n, int), ValueError(f"n must be an integer greater than 0, not {n}")

    if n == 1:
        return factorization
    else:
        for i in range(2, int(n**(1/2)+1)):
            if n%i == 0:
                new_factorization = factorization.copy()
                new_factorization[i] = new_factorization.get(i, 0) + 1
                return prime_factorization(int(n/i), new_factorization)
        factorization[n] = factorization.get(n, 0) + 1
    return factorization

def partitions(num):
    if num == 1:
        return [[1]]
    else:
        return [[num], *[[1, *p] for p in partitions(num-1)]]

def all_paths_through_list(l, paths=[[]]):
    """
    input l (list): a list with the following structure
    l = [ [a1, a2, a3, ...], [b1, b2, b3, ...], ... ]

    returns all paths from the first sublist to the last sublist,
    an example path would be [a1, b3, c2, ....]
    """

    if not l:
        return paths
    else:
        all_paths = []
        for item in l[0]:
            all_paths += all_paths_through_list(l[1:], [p+[item,] for p in paths])
        return all_paths

def abelian_groups(n):

    # get prime factorization as dictionary
    # n = {p1: a1, p2: a2, ...]
    pf = prime_factorization(n)

    # for each prime/power combo
        # generate the groups recursively... 
    dps_of_prime_powers = []
    for p, a in pf.items():
        dps_of_prime_powers.append([])
        for partition in partitions(a):
            relv_Gs = [CyclicGroup(p**i) for i in partition]
            if len(relv_Gs) == 1:
                dps_of_prime_powers[-1].append(relv_Gs[0])
            else:
                dp_for_partition = DirectProduct(*[CyclicGroup(p**i) for i in partition])
                dps_of_prime_powers[-1].append(dp_for_partition)

    all_paths = all_paths_through_list(dps_of_prime_powers)
    all_groups = [DirectProduct(*path) for path in all_paths]
    
    return all_groups
    # selecting the lists could potentially also be seen as
    # finding all topological orderings

if __name__ == "__main__":
    print([str(G) for G in abelian_groups(int(2e65))])
    #print(DirectProduct(*[CyclicGroup(12) for i in range(4)]))