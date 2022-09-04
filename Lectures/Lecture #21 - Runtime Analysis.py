# Lists and Slicing Lists
L = [5,6,7,3,5,6]
L[1:4:2]
L[5:2:-1]
L[3::-1]

# Aliasing

L = [1,2,3]
L1 = L # Both L1 and L refer to the same thing in the memory table

# binary search

def find_i_binary(L,e):
    low = 0  # 1 operation (ops)
    high = len(L) - 1 # 3 ops
    while high-low >= 2: # 3 ops
        mid = (low+high) // 2 # 3 ops
        if L[mid] < e: # 3 ops
            low = mid + 1 # 2 ops
        elif L[mid] > e: # 3 ops
            high = mid - 1 # 2 ops
        else:
            return mid # 1 ops

    if L[low] == e: # 3
        return low # 1
    elif L[high] == e: # 3
        return high # 1
    else:
        return None # 1

# Steps for finding complexity:
# 1. Find the # of operations the function takes (probably a function of the input, or the size of the input
# 2. Write down a simple form of an upper bound on (1) using big-Oh notation

# O(log(n)) where n = len(L)

# For the function find_i_binary():
# Worst case would be if plus elif plus one of the statements = 8
# 11 cause the while loop plus the 8
# Overall runtime in the worst case is 4 + 3+3+1 + k * 11
# k is the number of time the while loop repeats
# k = log2(n)
# therefore, runtime = 11 + 11 * log2n or 11 + 11 * log(n)* log 2/log e
# This is equal to O(log(n))



e = 200
L = [2,50,55,120,170,200,250]

