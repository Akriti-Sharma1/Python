# How efficient is the function f?
# For an input of size n, in the worst case, what is the runtime proportional to?

def f(L):
    if L[0] == 5:
        return
    for i in range(len(L)):
        for j in range(len(L)//2):
            print("hi") # const amt of time
# Total runtime = const1 + const*len(L)*len(L)//2
# The runtime is proprotional to n^2 where n = len(L)     (for large n)
# Asymptotic worst-case runtime complexity: O(n^2)

# Pythogiran triple, (a, b, c) such that a^2+b^2 = c^2
# For example, 3, 4, 5 is a Pythorean triple

# Want to write a function that searches for triples such that a^p + b^p = c^p

def fermat(p):
    n = 0
    while True:
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i**p + j**p == k**p:
                        return i, j, k
        n += 1
# Fermat's Last Theorem: a^p + b^p = c^p has no integer solutions for p >= 3

# Recursion: functions that call themselves
# n! = 1*2*3*4...*n
# 0! = 1
# n! = (1*2*3*...*(n-1))*n = (n-1)!*n

def fact(n):
    '''Return n!'''
    if n <= 1:
        return 1
    else:
        n * fact(n-1)



#fact(1)
#
#fact(n-2)
#   |
#fact(n-1)
#   |
#fact(n)

# Recursive function f:
# 1. Base case (an input where you know the output)
# 2. Recursive step (the answer in terms of the function f)

# Start from 0
# Each player can say either +1 or +2
# The first player to get to the sum 21 wins

def is_winning_sum(s):
    if s == 21:
        return True

    MOVES = [1,2]
    # if is_winning_sum(s+1) is True of is_winning_sum(s+2) is True, then is_winning(s) must be False
    for move in MOVES:
        if is_winning_sum(s+move):
            return False
    return True