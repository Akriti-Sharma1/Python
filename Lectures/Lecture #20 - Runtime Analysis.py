# Analysis of runtime complexity

def find_i(L, e):
    ''' Return the index of the first appearance of e in L, or None if e is
    not L'''
    # return L.index(e)
    for i in range(len(L)): # 1 op
        if L[i] == e: # 2 ops
            return i # 1 op

    return None # 1 op

# Worst-case runtime complexity: the runtime in the worst case, for input of size n

# worst case: e is not in L
#3*n + 1 operations
# the runtime will be proportional to (3*n+1)
# the runtime in the worst case, for large n, will be proportional to n
# The tight upper bound on the asymptotic runtime complexity of find_i is O(n)

# L is sorted
# [1,5,100,102,105,200,250,500,520,500]
# 520

# binary search

def find_i_binary(L,e):
    # currently looking at L[low]...L[high]
    low = 0
    high = len(L) - 1
    while high - low >= 2:
        mid = (low+high) // 2
        if L[mid] > e:
            high = mid - 1
        elif L[mid] < e:
            low = mid + 1
        else:
            return mid
        if L[low] == e:
            return low
        elif L[high] == e:
            return high
        else:
            return None