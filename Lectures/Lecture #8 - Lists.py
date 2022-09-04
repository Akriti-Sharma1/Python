# Lists

earnings = [91, 87, 115, 108]

len(earnings) # Length of the list

print(earnings)

for i in range(len(earnings)): # Prints over every item in the list
    print(earnings[i])

for amt in earnings: # Another way to print the list
    print(amt)

USD_TO_CAD = 1.25
for amt in earnings: # does not change the stuff in earnings (prior list)
    amt *= USD_TO_CAD
    print(amt)

for i in range(len(earnings)):
    amt = earnings[i]
    amt *= USD_TO_CAD
    print(amt)

for i in range(len(earnings)): # To change the actual stuff in earnings
    earnings[i] *= USD_TO_CAD

# Compute the number of trailing zeros in n! (without explicitly computing n!)

# n! = 1*2*3*4*5*...*10*11*12*...*(5*5)*26*...*124*(5*5*5)*126*...
# count the total multiplicity of 5

def multiplicity5(n):
    '''Return the multiplicity of 5 in n
    n is a positive intger'''

    count = 0
    while n % 5 == 0:
        count += 1
        n //= 5

    return count

def trailing_zeros_fast(n):
    '''Return the number of trailing zeros in n!'''
    total = 0
    for i in range(1, n+1):
        total += multiplicity5(i)

    return total

# Example 1:
def is_non_decreasing(L):
    ''' Return True iff the elements of L are arranged
    in non-decreasing order
    >>> is_non_decreasing([1,2,2,5])
    >>> True

    >>> is_non_decreasing([1,3,5,4,7])
    >>> False
    '''

    for i in range(1, len(L)):
        if L[i] < L[i-1]:
            return False

    return True

if __name__ == "__main__":
    print(is_non_decreasing([1,2,2,5]))
    print(is_non_decreasing([1,3,5,4,7]))

# Example 2:
def f(x):
    return x**2

L = [f, "abc", "ab", 5]

L = [42, 43, [45, 46], 47]

[45, 46][0] # To print the 0th item in the list

L = [[1, 2, 3, 4],
     [1, 0, 1, 0],
     [2, 2, 3, 5]] # To print, write [list index][element index]

L = [[[[[[[]]]]]]]

# Inserting elements:
L = [5,6,7,10,5]
# L.insert(ind, elem) # Insert elem before index ind
L.insert(2, 42)
L.insert(0, 43)
L.insert(len(L), 45) # To add at the end of the list
L.append(42) # Adds the element to the end of the list
print(L)

# Index return:
L = [5,6,7,10,5]
#L.index(elem) returns the index of the first appearance of elem in L
# Produces an error if there is no elem in the list L

L.index(5)
L.index(7)
print(L[L.index(7)]) # To actually print the element
#L.index(50)

# Check if elem is in List:
L = [5,6,7,10,5]
6 in L # True
8 in L # False

6 not in L # False
8 not in L # True

e = 6
if e in L:
    print("The element", e, "is in L")
else:
    print("The element", e, "is not in L")

# Range
for i in range(2,10,3): # range(stop, end, step)
    print(i)

list(range(2,10,3)) # To manually make a list

Lrange = []
for i in range(2, 10, 3):
    Lrange.append(i) # To make a list in loop

# Splicing:
L = [5, 6, 10, 12, 16, 17, 18, 20]
L[1:8:2] # L[start index: end index (not included): step]

Lslice = []
for i in range(1,8,2):
    Lslice.append(L[i])

# The default step is 1, The default starting index is 0, the default ending index is len(L) (unless step is negative)

L[:8:2]
L[::2]
L[::]
L[5,:]

L[5::-1]
L[::-1] # Reverse the list order

def slice_list(L, start, end, step):
    # Return L[start:end:step]
    for i in range(start, end, step):
        res.append(L[i])
    return L













