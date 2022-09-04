# swap the values of a and b without using a third temporary variable, and without multiple assignment

# a = a + b # a = old a + old b, b: old b
# b = a - b # a = old a + old b, b = new a - b (old a)
# a = a - b # a = new a - old a (old b), b = old a

# Boolean Functions
a = False
# and, or, not
not True
not False

not(1==1)

# A or B is True if at least one of A, B is True, False otherwise

True or False # True
False or True # True
True or True # True
False or False # False

# A and B is True if A and B are both True, False otherwise

True and True # True
False and True # False
True and False # False
False and False # False

(not(1!=1)) and (5>4) # True


# "For dessert I'll have pie or ice cream"

# Write and expression that's True if and only if one of pie or ice_cream is True, but not both

pie = True
ice_cream = True
# The expression should be False

pie = True
ice_cream = False
# the expression should be True
def did_i_lie(pie, ice_cream):

    if (pie or ice_cream) and not (pie and ice_cream):
        return "I had pie or ice cream"

    if pie != icecream:
        return "I had pie or ice cream"

# The english "or" is called "exclusive or"

# If you are operating on Booleans, you can use ^ for exclusive or

True or False and False
1    +   0     *   0 # Therefore, the 'and' has priority due to BEDMAS

True or True
1    +   1   # If it is positive, it is true, if it's 0, it's false

False or False
0     +   0

False or True
0     +   1


#Example 1:

# (A and B and C) == ((A and B) and C) == (A and (B and C))
lazy = False
smart = True
growthmindset = True

if not lazy and smart and growthmindset:
    print("EngSci")
elif lazy and smart:
    print("Physics")
elif not lazy and smart and not growthmindset:
    print("Econ")
else:
    print("Ryerson")

#Example 2:

def has_roots(a, b, c):
    '''Return True iff ax^2+bx+c has at least one real root'''
    disc = b**2-4*a*c
    return disc >= 0

def has_no_roots(a,b,c):
    return b**2-4*a*c > 0

def has_no_roots2(a,b,c):
    return not has_roots(a, b, c)

print(has_roots(1, 2, 3))

#Example 3

def artsie_math(arg1, arg2, op):
    '''For numbers arg1 and arg2, and operation op (a str), return arg1 op
    arg 2
    >> artsie_math(5,2,"+")
    7
    op can be + or - '''

    if op != "+" and op != "-":
        return None

    if op == "+":
        return arg1 + arg2
    elif op == "-":
        return arg1 - arg2
    #else:
       # print("I am an artsie, I only know + and -") # if this was a return it would not print the hi below

# If nothing is returned from the function, None is printed
# If a function f doesn't return anything explicitly, the value of f() is None

    print("hi")


if __name__ == '__main__':
    print(artsie_math(2,3,"+")) # 5
    print(artsie_math(2,3,"*"))
















