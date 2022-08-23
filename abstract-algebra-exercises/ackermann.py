# 2.4.2
"""
Write a program to evaluate Ackermann’s function A(x, y).
Modify the program to count the number of statements executed in the program when

A(0, y) = y + 1
A(x+1, 0) = A(x, 1)
A(x+1, y+1) = A(x, A(x+1, y))

Idea:
Since this type of notation is hard to read for programming, I'll use a change of variables. 

A(0, y) = y+1
A(x, 0) = A(x-1, 1)
A(x, y) = A(x-1, A(x, y-1))
"""

def A(x, y, steps=0):
    if x == 0:
        return y+1, steps+1
    elif y == 0:
        return A(x-1, 1, steps+1)
    else:
        r, inter = A(x, y-1, steps+1)
        return A(x-1, r, inter+1)

if __name__ == "__main__":
    x, y = [int(n) for n in input("Input two integers to compute A(x, y): ").split(',')]
    print(A(x, y))