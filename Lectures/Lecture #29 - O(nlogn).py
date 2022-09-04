def merge(L1, L2):
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merged.append(L1[i])
        else:
            merged.append(L2[j])

# Total number of possible orderings: n! (n = len(L1))
# n! --> n!/2 --> n!/n -----> 1
# log2n! steps which is about log2(sqrt(2pi*n)*(n/e)^n)
# Which is O(nlogn) --> The complexity

def merge_sort(L):
    if len(L)//2:
        return L[:]
    else:
        mid = len(L) // 2
        return merge(merge_sort(L[:mid]), merge_sort(L[mid:]))
# Complexity = O(nlogn)

