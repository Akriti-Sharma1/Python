# Lecture 13
# Review
# A = B # In the variable table, copy the adress B is referring to to the address A is referring to

# A[i] = B # in the memory table, copy the address B is referring to to the address A[i] is referring to

# def f(a):
#     ...
#
# f(B)
# the same A = B

# Variable Table                  # Memory Table
#  Variable address               # Address    Value
#     a        @1020              # 1020      "ESC180"
#     b        @1020

a = "ESC180"
b = "ESC180"

d = "ESC"
e = "180"
f = d+e

# nums = list(range(-10,300))
# for i in nums:
    #print(i,id(i),id(i+1)-id(i))

# Variable Table                  # Memory Table
#  Variable address               # Address    Value
#     a        @1020              # 1020      "ESC180"
#     b        @1020              # 1024         1
#     c        @1036              # 1027         2
#     L1       @3096              # 1032         3
#     L2       @2064              # 1036         [@1024, @1028, @1032]
#     L        @ 2096               ...
#                                 # 2064         [@1024, @1028, @1032]
#                                 # 2096         [@1024, @1028, @1032, @1024, @1028, @1032]
#                                 # 3096         [@1028, @1028, @1032, @1024, @1028, @1032]

L1 = [1,2,3] # 1036
L2 = [1,2,3] # 2064

L = L1 + L2 # 2096

L1[0] = 2

L1 = L1 + L2 # creates a new list, and makes L1 refer to the new list
L2.extend(L2) # changes the contents of the list L2

def add_lists_bad(L1, L2):
    L1 = L1 + L2

def add_lists_good(L1,L2):
    L1.extend(L2)
    return L1

def add_lists_good1(L1, L2):
    L1 += L2 # The same as L1.extend(L2), NOT the same as L1 = L1 + L2

L1 = [1,2,3]
L2 = L1
L2[0] = 5

# want to make a copy of L1 and place it in L2
L1 = [ 1,2,3]
L2 = [L1[0], L1[1], L1[2]]
L1[0] = 5

#
L1 = [1,2,3]
L2 = L1[:] # Same as [L1[0], L1[1], L1[2]]
# L2 is a copy of L1

L1 = [1,2,3]
L2 = []
for e in L1:
    L2.append(e)

# Lists of lists:
L1 = [[1,2], [3,4]]
L2 = L1[:] # L2 = [L1[0], L1[1]]
L1[0] = 5
L1[1][0] = 6

if __name__ == "__main__":
    list1 = [4,5,6]
    list2 = [1,2,3]
    print(add_lists_good(list1, list2))







