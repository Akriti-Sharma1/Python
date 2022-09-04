def print_list(L):
    '''Print the list L'''
    if len(L) == 1:
        print(L[0])
        return
    print(L[0])
    print_list(L[1:])

def print_list_rev(L):
    '''Print the list L in reverse'''
    if len(L) == 1:
        print(L[0])
        return
    print_list_rev(L[1:])
    print(L[0])

def sum_list(L):
    if len(L) == 0:
        return 0
    return L[0]+sum_list(L[1:])

def sum_list2(L):
    mid = len(L) // 2
    return sum_list2(L[:mid])+sum_list2(L[mid:])

def sum_list3(L, start, end):
    ''' Return sum(L[start, end+1])'''
    if start == end:
        return L[start]
    return L[start] + sum_list3(L,start+1, end)

# # of calls: n
# Each call takes k time
# Total runtime: kn --> O(n)

def sum_list4(L):
    if len(L) == 0:
        return 0
    return sum_list3(L,0,len(L)-1)

sum_list3([1,2,3,4,5],1,5)


print(sum_list([1,2,3,4,5]))