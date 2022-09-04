# Lecture 12
# Variable table                           Memory Table
#
# Variable Address                          address     value
#------------------                       -------------------
#    n      @1028                           1024
#    m      @1040                           1028         42
#    L1     @2040                           1032
#     L     @1036                           1036         [@1028, @1032]
#                                           1040         500
#                                           2040         [@1040, @1040]

def change_list(L):
    L[0] = 5

def dont_change_list(L):
    L = [50]

def dont_change_int(n):
    n = 50

def ch_list(L1):
    L1[0] = 400
    L1 = [500, 500]

if __name__ == "__main__":
#     n = 42
#     print(n)
#     m = n
#     m = 500
#     id(n) # the actual address where n is located
#
#     L = [42, 500]

    L = [500,400]
    ch_list(L)

    L1 = [1,2,3]
    change_list(L1)
    print(L1)

    dont_change_list(L1)
    print(L1)


    #L1[0] = 500 # Also changed L[0]
    # Aliasing: several variables refer to the same object
    # If we change the contents of L, the contents of L1 change as well and vice versa

    # Objects whose contents can change (e.g. lists) are MUTABLE
    # Objects whose contents cannot change (e.g. ints, strs, floats) are IMMUTABLE

