# Lecture 11
# Missing k problem
# 1...n, k is missing, we want to find k efficiently

# 1 + 2..+n = n(n+1)/2
# n(n+1)/2 - (1 + 2 + ... + n) = k

def missing_k():
    cur_sum = 0
    for e in L:
        cur_sum += e

    n = len(L) + 1

    return n*(n+1)//2 - cur_sum

# print vs return

def f(n):
    n = n * 2
    return n + 5

def f_print(n):
    n = n + 2
    print(n+5)

def first_two_evens(L):
    ''' Return the first even number in the list L'''
    res = []
    for e in L:
        if e % 2 == 0:
            res.append(e)
    return res[:2]

def first_two_evens_efficient(L):
    ''' Return the first even number in the list L'''
    res = []
    for e in L:
        if e % 2 == 0:
            res.append(e)
            count += 1
            if count == 2:
                return res
    return res # of length 0 or 1

if __name__ == "__main__":
    print(f(50))
    print(f_print(50))
    print(first_two_evens([1,5,7,8,1,10,12]))

# Nested Loops
counter = 0
for i in range(3):
    for j in range(2):
        counter += 1
        print(i,j,counter)

# Unrolling the Loop
i = 0
for j in range(2):
    counter += 1
    print(i,j,counter)

i = 1
for j in range(2):
    counter += 1
    print(i,j,counter)

i = 2
for j in range(2):
    counter += 1
    print(i,j,counter)

# Write loops as a function
def iter_j(i):
    global counter
    for j in range(2):
        counter += 1
        print(i,j,counter)

def iter_j_A(i, counter):
    for j in range(2):
        counter += 1
        print(i,j,counter)

for i in range(3):
    iter_j(i)

# Example of nested loops
def login(username, password):
    if username == "guerzhoy" and password == "abad":
        return True
    else:
        return False

# Suppose we know the passowrd is of length 4
if __name__ == "__main__":
    for letter1 in ["a","b","c","d","e","f"]:
        for letter2 in ["a","b","c","d","e","f"]:
            for letter3 in ["a","b","c","d","e","f"]:
                for letter4 in ["a","b","c","d","e","f"]:
                    password = letter1 + letter2 + letter3 + letter4
                    #print("Trying password,", password)
                    if login("guerzhoy", password):
                        print(password)
    counter = 0
    for i in range(3):
        iter_j(i)

# want to know whether the list L contains duplicate elements

def has_duplicates1(L):
    '''
    >>> has_duplicates([5, 1, 3, 1, 6])
    True
    >>>
    has_duplicates([5, 1, 3, 6])
    False
    '''

    for i in range(len(L)):
        if L[i] in L[i+1:]:
            return True

    return False

def has_duplicates2(L):
    sorted_L = sorted(L)
    for i in range(1, len(L)):
        if L[i] == L[i-1]:
            return True
    return False

sq = [[2, 9, 5],
     [1,2,5],
     [7,8,7]]

def has_duplicates_sq(L):
    flat_sq = []
    for line in sq:
        flat_sq.extend(sq)
    return has_duplicates2(flat_sq)

















