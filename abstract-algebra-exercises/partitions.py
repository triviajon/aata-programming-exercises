# 14.5

"""
Write a program to compute the number of conjugacy classes
in Sn. What is the largest n for which your program will work?
"""

"""
Thought process:

We know that the number of conjugacies classes in Sn is the same as
the number of cycle decompositions of Sn. This is proved in one of my
LaTeX documents available soon on my website. https://triviajon.com/

This number is P(n), or the number of partitions of the integer n. 

Thus, we just need to write a function to compute the number of partitions of n.

This problem is proven to be NP-hard, so the following algorithm is not 
efficient, and it is likely there will be no algorithm to quickly calculate
the number of partitions of n.
"""

def get_partitions(n):
    memotable = {(1, k): set() for k in range(1, n+1)}
    memotable.update({(m, k): set() for k in range(1, n+1) for m in range(1, k+1)})
    memotable.update({(0, k): set(((),),) for k in range(n+1)})
    memotable.update({(1, 1): {(1,)}})

    for m in range(2, n+1):
        for k in range(1, m+1):
            memotable[(m, k)] = {(kprime, *p) for kprime in range(k, m+1) for p in memotable[m-kprime, kprime]}
    return memotable[n, 1]


if __name__ == "__main__":
    user_int = int(input("What is your input: "))
    pp.pprint(len(get_partitions(user_int)))    