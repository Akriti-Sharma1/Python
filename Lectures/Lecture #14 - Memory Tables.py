L1 = [1,2,3]
L2 = L1
L2[0] = 5 # also affects L1[0]

L1 = [1,2,3]
L2 = L1[:] # same as L2 = [L1[0], L1[1], L1[2]]
L2[0] = 5 # does not affect L1[0]

L1 = [[1, 2], [3,4]]
L2 = L1[:] # same as L2 = [L1[0], L1[1]] # as if we said L2[0], L2[1] = L1[1]
L2[0][0] = 5 # changes L1[0][0] as well
L2[0] = 7 # L2 is now [7, [3,4]], L1 is still [[5,2], [3,4]]

L1 = [[1, 2], [3,4]]
L2 = []
for sublist in L1:
    L2.append(sublist[:])

L2[0][0] = 5 # does not affect L1[0][0]

