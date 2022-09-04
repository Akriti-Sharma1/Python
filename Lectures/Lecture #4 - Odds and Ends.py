#Odds and Ends
#Multiple Assignments

a = b #assignment
a1, a2 = b1, b2 # the same as put b1 in a1, put b2 in a2

a = 3
b = 4
a, b = b, a # a is 4, b is 3, preferred way of swapping the value of variables

#Couldn't translate this to a = b, b = a

# Swap the values of a and b without multiple assignment
temp = a # temp has old value of a, a has old value of a, b has old val of b
a = b # temp has old value of a, a has old value of b, b has old val of b
b = temp # temp has old value of a, a has old value of b, b has old val of a

# Swap the 2 values of a, b without multiple assignment, and without using an extra variable
# b = a + b
# a = ...


# Converting objects to different types

# int, float, str, bool

int(3.14) #converting to int (rounds down)

str(3.14) #is "3.14"

s2 = "The value of pi is approx " + str(3.14)

bool('asdf') #True
bool('zero') #True
bool(0) # False
bool("") # False (empty string)

int("35")
float("35.4")

if "abc": # String converts to true (will print regardless)
    print("hi")

# Function Example #1
def adjust_grade():
    global grade
    grade = grade - 5
    print("New grade inside the function:", grade)

if __name__ == "__main__":
    grade = 95
    adjust_grade()
    print("New grade outside the function:", grade)

#Global variable grade, which the function adjust_grade changes

#Function Example #2
def adjust_grade2(grade):
    grade = grade - 5
    print("New grade inside the function:", grade) #90

if __name__ == "__main__":
    grade = 95
    adjust_grade2(grade)
    print("New grade outside the function:", grade) #95

# The global variable is not changed as it is not declared

#Function Example #3
def adjust_grade3(g):
    g = g - 5
    print("New grade outside the function:", grade)

if __name__ == "__main__":
    grade = 95
    adjust_grade3(grade)
    print("New grade outside the function:", grade) #95

#Function Example #4
def adjust_grade4(g):
    global grade #access global variables: globals(), locals()
    grade = g - 5

if __name__ == "__main__":
    grade = 95
    adjust_grade4(grade)
    print("New grade outside the function:", grade)

#Function Example #5
def get_adjusted_grade(grade):
    return grade - 5 #90

if __name__ == "__main__":
    grade = 95 # 95
    get_adjusted_grade(grade)
    print("New grade outside the function:", grade) # 95

# Function Example #6
def get_adjusted_grade(grade):
    return grade - 5

if __name__ = "__main__":
    grade = 95
    grade = get_adjusted_grade(grade)
    print("New grade outside the function:", grade) #90

# Function Example #6
def adjust_grade_error():
    grade = grade - 5 #ERROR
    print("New grade inside the func:", grade)

if __name__ == "__main__":
    grade = 95
    grade = adjust_grade_error()

# Function Example #7
def minus5(x):
    global ret_val_minus5
    ret_val_minus5 = x - 5

if __name__ == "__main__":
    minus5(10)
    print("Result:", ret_val_minus5)

#



















