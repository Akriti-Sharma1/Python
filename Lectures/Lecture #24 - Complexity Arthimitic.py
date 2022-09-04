# Counting Sort Algorithm
def counting_sort(L):
    # m = max(L), n = len(L)
    max_int = max(L) # O(n), k1*n time, for some k1

    counts = [0] * (1 + max_int) # O(m), k2*m time, for some k2

    for e in L:
        counts[e] += 1 # O(n), k3*n time

    sorted_L = []
    for i in range(0, len(counts)):
        sorted_L.extend([i]* counts[i]) # O(n), k4*n, because we're extending sorted_L by n elements in total, and the loops itself runs (m+1) times

    L[:] = sorted_L # k6 * n

# Total: (k1+k3+k4+k6)*n + (k2+k5)*m time
# O(n+m)

def is_sorted_nondecreasing(L):
    ''' Return True if L is sorted in non-decreasing order'''
    # return L == sorted(L)
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            return False
    return True

import random

def bozosort(L):
    while not is_sorted_nondecreasing(L):
        i, j = int(len(L)*random.ranom()), int (len(L)*random.random())
        L[i], L[j] = L[j], L[i]
# n! permutations of L
# O(n!)

# Complexity Arithmitic
# In general, we assume that there is an upper bound on input numbers
# True of floats but not true of integers

# Want to add 2 n-digit integers:
    abcdfsdf
   +asdfdsf
   ----------
# Addition is O(n), where n is the number of digits
# The number of digits n is approx log_10 N, where N is the integer

abcnda
ajskdlfj
x--------
 djfkdsl
jdfsljkl
---------
dslfj
---------
# Approx n^2 multiplicatins, n^2 additions
# In general O(n^2) where n is the number of digits

# Karatsuba Algorithm takes approx O(n^1.68)
