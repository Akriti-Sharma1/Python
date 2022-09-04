def power(x, n):
    if x == 1 or n == 0:
        return 1
    else:
        return x * power(x,n-1)

#print(power(2,3))

new = []
def print_lists(L1, L2):
    #new = []
    if len(L1) == 1:
#         print(L1[0])
#         print(L2[0])
        new.append(L1[0])
        new.append(L2[0])
        print(new)
    else:
        #print(L1[0])
        #print(L2[0])
        new.append(L1[0])
        new.append(L2[0])
        print_lists(L1[1:], L2[1:])
# Return list with the recursion
#Return [...] + interleave(...)

#print_lists([1,3,5],[2,4,6])

def reverse_rec(L):
    '''Print the list L in reverse'''
    if len(L) == 1:
        print(L[0])
        return
    reverse_rec(L[1:])
    print(L[0])
#reverse_rec([1,2,3,4,5,6])

#Without using loops and without ever using print with a list (as opposed to individual elements of a list), write a function that, given a list L of size n (assume n is odd), prints the elements of L in the following order
def print_list(L):
    if len(L) == 1:
        print(L[0], end = "")
    else:
        print(L[len(L)//2])
        L.pop(len(L)//2)
        print_list(L)

#print_list([1,2,3,4,5,6,7])

#Without using any loops or global variables, write a function the with signature (exactly, without default parameters) is_balanced(s) which returns True iff the string s is has “balanced” parentheses, i.e., all parentheses () in string s match exactly. For example, "(()(()))" is balanced but the following: "(well (I think), recursion works like that (as far as I know)" is not, since it’s missing a closing parenthesis. To simplify matters, you may start by thinking about strings that contain only parentheses, but your final function should work with all strings. Your function should only care about balancing parentheses (), not brackets [] or braces {}. You may use str.find and str.rfind, or (recursive) helper functions.
def is_balanced(s):
    s = list(s)
    print(s)
    if len(s) == 0:
        return True
    elif "(" in s and ")" not in s:
        return False
    elif "(" not in s and ")" in s:
        return False
    else:
        #print(s)
        s.remove("(")
        s.remove(")")
        is_balanced(s)

#is_balanced(s[:open_index] + s[close_index+1:])

print(is_balanced("(()"))


