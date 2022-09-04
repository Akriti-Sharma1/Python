#Example of if statements:
#Goes top to bottom and triggers first condition that is met

# exam_grade = 97
#
# if exam_grade == 98:
#     print("I won the bet")
#     print("I am happy")
# elif exam_grade > 98:
#     print("I am happy")
# else:
#     print(")-:")

#print("hi") #Outside the if statements as not indented; will be printed regardless

#Example 2:
# shillings = 2
# name = "Jack Sparrow"
# greeting = "Welcome to Port Royal, "
#
# if shillings >= 3:
#     print(greeting + "Mr. Smith.")
# elif shillings >= 1:
#     print(greeting + name)
# else:
#     print("Go away please.")

# To run a portion of the code, just hilight desired code and press ctrl + enter
# To comment a portion of the code, just highlight desired code and press ctrl + shift + 3

#Example 3: Program that computes the roots of the equation ax^2+bx+c
# import math #used for sqrt
#
# a = 1
# b = 2
# c = 5
#
# disc = b**2 - 4 * a * c #exponent formatting is x**n
#
# if disc > 0: # two roots
#     r1 = (-b - math.sqrt(disc)) / (2*a)
#     r2 = (-b + math.sqrt(disc)) / (2*a)
#     print (r1, r2, sep = ", ")# print(1, 2, 3, sep = " ! ")
# elif disc == 0:
#     print(-b/(2*a))
# else:
#     print("There are no roots")

# Writing a function:
def my_add(a,b): #define a function using def and then the name
    res = a + b #indent the rest of the code to keep it inside the function
    print(res)
    return res # value of the function

print(2 * my_add(10,12)) #print this outside the function











