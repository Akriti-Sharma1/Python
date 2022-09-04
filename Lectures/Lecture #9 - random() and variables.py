import random

x1 = random.random() # Random between 0 and 1, not including 1
x2 = random.random()

x1, x2 = random.random(), random.random()

# is (x1, x2) inside the quarter circle?

# x1**2 + x2**2 < 1 <=> (x1, x2) is inside the unit circle

def approx_pi(n_points):
    count = 0

    for i in range(n_points):
        x1, x2 = random.random(), random.random()
        if x1**2 + x2**2 < 1:
            count += 1

    return 4 * count / n_points

# pseudo-random numbers
# a sequence of numbers that have random-like properties
# x, f(x), f(f(x)), f(f(f(x))), ....

# Make f(x) = (324872983*x % 59) (59 is random prime number, thats not divisible)
# This will produce random numbers in the range 0 to 58 (inclusive)

def f(x):
    return 324872983*x % 59

def my_random():
    global x
    x = f(x)
    return x / 59

def init_random():
    global x
    x = 3

init_random()

if __name__ == '__main__':
    print(my_random())
    print(my_random())
    print(my_random())
    print(my_random())

# Lists

L = [5,7,10,3,5,20,15]

# L[start:end:step]
L[1:6:2]

def manual_slice(L, start, end, step):
    '''Return L[start:end:step]'''

    res = []
    for i in range(start, end, step):
        res.append(L[i])

def manual_slice_while(L, start, end, step):
    '''Return L[start:end:step]'''
    res = []
    i = start
    if step > 0:
        while i < end:
            res.append(L[i])
            i += step

    else:
        while i > end:
            res.append(L[i])
            i += step

#     # Alternatively:
#     while (step > 0  and i < end) or (step < 0 and i > end):
#             res.append(L[i])
#             i += step

# Extend:
# L.extend(L1) appends all the elements of L1 to L

L = [5,6,7]
L1 = [3,4]
L.extend(L1)
print(L)

L = [5,6,7]
L1 = [3,4]
L.append(L1)
print(L)

# Slicing for extending lists "in the middle"

L = [42, 43, 45]
M = [51, 52]

L[1:1] = M #(Inserts a list into a list)

L = [42, 43, 45]
M = [51, 52]
L[1] = M

L = [42, 43, 45]
M = [51, 52]
L[1:2] = M # Splicing (Replaces a part of the list with another list)

# Sort lists:
L = [5, 1, 10, 12, 4]
L.sort() # L becomes a sorted version of itself, increasing

L = [3,5,2]
sorted(L) # This does not change L, creates a new list that is sorted

# Cannot do sorted([1, "a", "hi"])

sorted(["PHY", "CIV", "ESC"]) # Alphabetical order

[1, 2, 3] + [7, 8] # List is not mutated, a new list is created

L1 = [1, 2, 3]
L2 = [7,8]
L3 = L1 + L2 #L1.extend(L2) changes L1

L1 = [1, 2, 3]
L2 = [7,8]

L1 += L2 # Exactly the same as L1.extend(L2), not exactly the same as L1 = L1 + L2















