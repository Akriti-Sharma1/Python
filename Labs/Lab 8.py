import numpy as np


# # Printing matrices using NumPy:
#
# # Convert a list of lists into an array:
# M_listoflists = [[1,-2,3],[3,10,1],[1,5,3]]
# #M = np.array(M_listoflists)
# # Now print it:
# #print(M)
#
#
#
#
# #Compute M*x for matrix M and vector x by using
# #dot. To do that, we need to obtain arrays
# #M and x
# #M = np.array([[1,-2,3],[3,10,1],[1,5,3]])
# x = np.array([75,10,-11])
# #b = np.matmul(M,x)
#
# #print(M)
# #[[ 1 -2  3]
# # [ 3 10  1]
# # [ 1  5  3]]
#
# # To obtain a list of lists from the array M, we use .tolist()
# M_listoflists = M.tolist()
#
# #print(M_listoflists) #[[1, -2, 3], [3, 10, 1], [1, 5, 3]]

def print_matrix(M_lol):
    M_lol = np.array(M_lol)
    print(M_lol)

def get_lead_ind(row):
    for i in range(len(row)-1):
        if row[i] != 0:
            return i
    return len(row)

def get_row_to_swap(M, start_i):
#     index = len(M)
#     checker = len(M)-1
#     for i in range(start_i, len(M)-1):
#         for j in range(len(M[i])-1):
#             if M[i][j] < index:
#                 index = i
#         # if get_lead_ind(M[i]) == len(M[i]):
#         #     index = 0
#         # else:
#         #     if get_lead_ind(M[i]) < index:
#         #         index = get_lead_ind(M[i])
#         #         checker = i
#     return index
    index = len(M)
    new = []
    for i in range(start_i, len(M)):
        new.append(get_lead_ind(M[i]))
    return start_i + new.index(min(new))

def add_rows_coefs(r1,c1,r2,c2):
    # Write a function with the signature add_rows_coefs(r1, c1, r2, c2) which takes in rows (represented as lists of equal lengths) r1 and r2 and coefficients (floats) c1 and c2, and returns a new list that contains the row c1*r1 + c2r2. (N.B.: to create a new list of 10 zeros, you can use [0]*10.)
    new = [0] * len(r1)
    for i in range(len(new)):
        new[i] += r1[i] * c1 + r2[i] * c2
    return new

def eliminate(M, row_to_sub, best_lead_ind):
#     c1 = M[row_to_sub+1][best_lead_ind]
#     c2 = M[row_to_sub+2][best_lead_ind]
#     print(c1,c2)
    #for i in range(best_lead_ind-1, len(M)-1):
    for i in range(len(M) - (row_to_sub+1)):
        c1 = -(M[row_to_sub+1+i][best_lead_ind]/M[row_to_sub][best_lead_ind])
        M[row_to_sub+1+i] = add_rows_coefs(M[row_to_sub],c1,M[row_to_sub+1+i],1)


# Write a function with the signature forward_step(M) which takes in an arbitrary matrix M (as a list of lists), applies the forward step of Gaussian Elimination to it, and modifies M to be the matrix obtained after the forward step is applied. This can be done by repeatedly calling get_row_to_swap, swapping rows, and calling eliminate. Unlike with ESC103, I recommend that you keep the entire matrix rather than extracting submatrices. The process of performing the forward step remains essentially the same. The process is illustrated on the next page. As you write forward_step(), add print() statements to forward_step() to produce output similar to the examples provided on this handout (i.e, print out the matrix transformation process, and comments on what’s happening at every step).

def forward_step(M):
    for i in range(len(M)):
        print_matrix(M)
        swapper = get_row_to_swap(M,i)
        M[i], M[swapper] = M[swapper], M[i]
        eliminate(M,i,get_lead_ind(M[i]))
    print_matrix(M)

def backward_step(M):
    for i in range(len(M)-1,-1,-1):
        best_lead = get_lead_ind(M[i])
        for j in range(i-1,-1,-1):
            c1 = -(M[j][best_lead]/M[i][best_lead])
            M[j] = add_rows_coefs(M[i], c1, M[j], 1)
            print_matrix(M)
    for i in range(len(M)):
        lead = M[i][get_lead_ind(M[i])]
        for j in range(len(M[i])):
            M[i][j] /= lead
            print_matrix(M)

def solve(M,b):
    augment = M[:]
    count = 0
    for row in augment:
        row.append(b[count])
        count += 1
        forward_step(augment)
        backward_step(augment)
        x = []
        for row in augment:
            x.append(row[-1])
        return x







if __name__ == "__main__":
    #print_matrix([[1,-2,3],[3,10,1],[1,5,3]])
    #print(get_lead_ind([1,-2,3]))
#     M = [[0, 6, 7, 8],
#     [1, 0, 1, 1],
#     [0, 0, 5, 2],
#     [0, 0, 7, 0]]
    M = [[0, 0, 0, 8],
        [1, 0, 5, 2],
        [0, 1, 1, 1],
        [0, 2, 7, 0]]
#     M = [[1, 0, 0, 0],
#             [0, 0, 0, 1],
#             [0, 0, 1, 0],
#             [0, 1, 0, 0]]
    start_i = 1
    #print(get_lead_ind([0,0,0,0]))
    #print(get_row_to_swap(M, start_i))
    # r1 = [5,6,7,8]
    # r2 = [0,0,0,1]
    # print(add_rows_coefs(r1, 2, r2, 2))
    #print_matrix(eliminate(M, 2, 1))
    #print_matrix(eliminate(M, 2, 3))
    forward_step(M)
    print_matrix(M)


