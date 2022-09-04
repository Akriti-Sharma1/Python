# dict.get()
d = {1:2, 3:4}
k = 10
if k in d:
    print(d[k])
else:
    print(k, "is not in the dictionary")

k = 1
d.get(k,42)

# dict.update()
d = {1:2, 3:4}
to_add = {5:6,3:5}
d.update(to_add)
print(d) # can be used to overwrite things

# Deep copy
obj = [[1,2],[[5,6],2],[1,[5,6]]]

def deep_copy(obj):
    '''Return a deep copy of obj
    obj is a list of nested lists that contain ints or an int'''
    if type(obj) == int:
        return obj
    copy = []
    for elem in obj:
        copy.append(deep_copy(elem))
    return copy

# Merge Sort
def merge(L1,L2):
    merged = []
    i, j = 0, 0
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merged.append(L1[i])
            i += 1
        else:
            merged.append(L2[j])
            j += 1
    merged.extend(L1[i:])
    merged.extend(L2[j:])

# Runtime complexity is O(len(L1) + len(L2))

def merge_sort(L):
    if len(L) == 1:
        return L[:]
    else:
        mid = len(L) //2
    return merge(merge_sort(L[:mid])), merge_sort(L[mid:])

# Complexity =