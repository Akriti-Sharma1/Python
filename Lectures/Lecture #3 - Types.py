#Values include 5, "hello", 3.2
#If you write a = 5, type(a) will return int
#type(6) will return int as well
#type(4/2) is float; type(4//2) is an int --> doesn't work for negative numbers
# """ line 1
# line 2
# line 3 """ # Must use """ for multi-line string
# print("line one\nline two") #use \n for next line
# print("Artscis are 'smart'") #For usage of quotations in strings
# print("line one \\n line two") #To display the \n
#
# #Booleans are either true or false
# a = (6>5) # example of boolean
# b = (2==3) #example of boolean
# a = 5
# b = 6
# c = b > a
# if c:
#     print("HI")

# def pirate_print(s):
#      print("Ahoy! " + s + "Arr!") #Function that has an effect
#
# pirate_print("I <3 Praxis! ")
# def piratify(s):
#     return "Ahoy!" + s + "Arr!" #Function that has no direct effect

# def has_roots(a,b,c):
#     """ Return True iff ax+bx+c=0 has at least one real root""" #Dock string that describes what a function does
#     disc = b**2 - 4 * a * c #Special local variables only defined within the function
#     if disc >= 0:
#         return True
#     else:
#         return False
#
# help(has_roots) #Help function? Gives the dock string back
# has_roots(1,2,1)

# def plunder_grade():
#     global grade #To declare a global variable within the function
#     grade = 79
#
# #grade = 97 #global variable outside the function
# plunder_grade()
# print(grade)

#Convention: Functions defined at the top of the file
# def f(x):
#     return x**2
# if __name__ = '__name__'
#     print(f(x))












