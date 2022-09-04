# N = 3
# f("aa")
# f("bc")
# f("de") # "aa" or "bc" or "de" with prob 1/3 each
# f cannot store more than a constant number of strings

# Sorting Algorithms
# Mutate the list C so that it's sorted in non-decreasing order
L.sort()

# Selection sort / Max sort
# Find the nth largest element in L and swap it with L[len(L)-1]
# Find the (n-1)st element in L and swap it with L[len(L)-2]
#.
#.
#Find the 2(n-1) element in L and swap it with L[1]

# [2,5,1,10,7] --> [2,5,1,7,10] --> [2,5,1,7,10] --> [2,1,5,7,10] --> [1,2,5,7,10]

def loc_max(L, end):
    ''' Return the location of the max in L[:(end+1)]'''
    cur_max = L[0]
    cur_max_loc = 0
    for i in range(1,end+1):
        if L[i] > cur_max:
            cur_max = L[i]
            cur_max_loc = i
    return cur_max_loc
    # Runtime Analysis = C1 + C2*end

def selection_sort(L):
    for i in range(len(L)-1):
        max_i = loc_max(L,len(L)-1-i)
        L[max_i], L(len(L)-1-i) = L(len(L)-1-i), L[max_i]
        # Runtime Analysis = C3 + (C1 + C2*(len(L)-1-0)
        #                  = C3 + C1 + C2*(len(L)-1-1)
        #.
        #.
        #                  = C3 + C1 + C2*1

# n = len(L)
# C3 * (n-1) + C1 * (n-1) + C2 * (1+2+3+4+...+(n-1))
# 1+2+ ... + k = k(k+1)/2
# Therefore, (n-1)(C1+C3) + C2 (n(n-1))/2
# = (C1+C3-C2/2)n - C2/2 + C2/2*n^2 is O(n^2)

# Bubble Sort
# [5, 2,3,6,0] --> [2,5,3,6,0] --> [2,3,5,6,0] --> [2,3,5,6,0] --> keep swapping different elements until they are in order (basically comparing side by side elements (called a sweep))

def bubble_sort(L):
    for i in range(len(L)-1):
        swapped = False
        for j in range(len(L)-1-i):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
                swapped = True
        if not swapped:
            break
   # Runtime Analysis: n = len(L)
  #                   =C0 + C1(n-1)(n+2)+...+1
  #                   =C0 + C1((n(n-1))/2)
  #                   =O(n^2)



