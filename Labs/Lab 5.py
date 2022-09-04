# Problem 1
# Write a function with the signature def list1_starts_with_list2(list1, list2), which returns True iff list1 is at least as long as list2, and the first len(list2) elements of list1 are the same as list2. Note: len(lis) is the length of the list lis, i.e., the number of elements in lis.

def list1_starts_with_list2(list1, list2):
    n = len(list1)
    if len(list1) <= len(list2):
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False
        return True
    return False

# Problem 2
# Write a function with the signature def match_pattern(list1, list2) which returns True iff the pattern list2 appears in list1. In other words, we return True iff there is an i such that 0≤i≤len(list1)-len(list2) and
#
# list1[i] = list2[0]
# list1[i + 1] =list2[1]
#     .
#     .
#     .
# list1[i + len(list2) – 1] = list2[-1]
#
# For example, if list1 is [4, 10, 2, 3, 50, 100] and list2 is [2, 3, 50], match_pattern(list1, list2) returns True since the pattern [2, 3, 50] appears in list1.
def match_pattern(list1,list2):
    j = 0
    if len(list2) > len(list1):
        return False
    else:
        for i in range(len(list2)):
            n = list2[j]
            if list1[i] == n:
                j += 1
            else:
                j = 0

        if j > 0:
            return True
        else:
            return False
        return True

# Problem 3
# Write a function with the signature def repeats(list0), which returns True iff list0 contains at least two adjacent elements with the same value.\
def repeats(list0):
    counter = None
    for i in list0:
        if list0[i] == counter:
            return True
        else:
            counter = list0[i]
    return False

#
# Problem 4
# In Python, you can use a list of lists to store a matrix, with each inner list representing a row. For example, you can store the matrix
#
# (506−375)
# by storing each row as a list: M = [[5, 6, 7], [0, -3, 5]]. For ease of reading, since Python allows for line breaks inside brackets, you can write it as follows:
#
# M = [[5,  6, 7],
#      [0, -3, 5]]
#
#
# You can use M[1] to access the second row of M (i.e., [0, -3, 4]), and you can use M[1][2] to access the third entry in the second row (i.e., 5).
#
# Problem 4(a)
# Write a function with the signature def print_matrix_dim(M) which accepts a matrix M in the format above, and prints the matrix dimensions. For example, print_matrix_dim([[1,2],[3,4],[5,6] ]) should print 3x2.

def print_matrix_dim(M):
    return str(len(M)) + "x" + str(len(M[0]))



# Problem 4(b)
# Recall that the product of a matrix M of dimension (n,m) and a vector v of dimension (m,1) can be written as
# Mv=⎛⎝⎜⎜⎜⎜(∑mi=1M1,ivi)......(∑mi=1Mn,ivi)⎞⎠⎟⎟⎟⎟.
# Write a function with the signature def mult_M_v(M, v) which returns the product Mv of a matrix M and a vector v. Vectors are stored as lists of floats.
#
# To write this function, you will need to create a new vector. Here are two ways to create a new vector (stored as a list) with 10 zeros in it:
#
# ten_zeros1 = [0]*10
#
# ten_zeros2 = []
# for i in range(10):
#   ten_zeros2.append(0)

def mult_M_v(M,v):
    L = []
    n = 0
    for i in range(len(v)):
        for j in range(len(v)):
            n += M[i][i]*v[i]
        L.append(n)
        n = 0
    return L


# Problem 4(c) (challenge)
# Write a Python function to perform matrix multiplication.

if __name__ == "__main__":
    #print(list1_starts_with_list2([1,2,3,4], [1,2,3,6,4]))
    #print(match_pattern([4, 10, 2, 3, 50, 100],[2, 3, 50]))
    #print(repeats([0,1,1,3]))
    #print(print_matrix_dim([[1,2],[3,4],[5,6,],]))
    print(mult_M_v([[1,2],[3,4],[5,6]], [1,2,3]))
