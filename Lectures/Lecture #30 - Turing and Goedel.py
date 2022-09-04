# Turing's Halting Problem and Goedel Incompleteness Theorem
# Enigma machine

'''def f():
    while True:
        pass'''

'''def g():
    n = 3
    while True:
        if n % 2 == 0 and is_prime(n):
            return
        n += 1'''

'''def fermat(p):
    n = 1
    while True:
        for i in range(1,n):
            for j in range(1,n):
                for k in range(1,n):
                    if i**p + j**p == k**p:
                        return i,j,k
        n += 1'''

def halt(f,x):
    ''' Return True if f(x) halts, and False if f(x) produces an infinite
    loop'''
    pass


def confused(f):
    if halt(f,f):
        while True:
            pass
    else:
        return False

# confused(confused) halts => halt(confused, confused) must be False
                        #  => confused(confused) produces an infinite loop
                        # Contradiction

# confused(confused) doesn't halt => halt(confused, confused) must be True
                                # => confused(confused) halts
                                # Contradition
# This means the assumption (halt(f,x)) is false.

def f():
    return None

import inspect
inspect.getsource(f)

## Goedel's Incompletness Theorems

# There are true mathematical statements that cannot be proven
# Suppose that every true mathematical statement can be proven
# We'll prove that it follows that we can write halt

def halt(f,x):
    # Generate all string over the latin alphabet of length 1, 2, 3, 4...
    # For every such string s
    #   if s is a proof that f(x) halts, return True
    #   if s is a proof that f(x) doesn't halt, return False
    pass

# So halt is impossible to write. Contradiction!
# So the assumption that every true mathematical statement can be proven is False

