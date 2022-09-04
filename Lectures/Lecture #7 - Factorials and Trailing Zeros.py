# Factorials and Trailing Zeros

# n! = 1 * 2 * 3 * ... * n
# Compute the number of trailing zeros in n!

# Compute n!
# Keep dividing a by 10 when it's possible
# Count the number of times we divided a by 10

def fact(n):
    '''Return n!
    n is a positive integer'''

    res = 1
    for i in range(1, n+1):
        res *= i

    return res

def trailing_zeros(n):
    fact_n = fact(n)
    counter = 0
    while fact_n % 10 == 0:
        fact_n //= 10
        counter += 1

        # Before we enter the loop:
        # fact_n has k trailing zeros and counter = 0
        # Every time we execute the block in the while loop, fact_n gets has one fewer trailing zero and counter increases by 1
        # trailing_z goes k, k-1, k-2, ... 0 and counter goes 0, 1, 2, ..., k

    return counter

# Write a function named login
# The function takes in a user name and a password
# Return "OK" if the username matches the password, unless there are 3 successiver failed login attepmts.
# Return "Refuse" otherwise.

def login(username, password):
    global failed_login
    if failed_login >= 3:
        return "Refused"

    if username == "guerzhoy" and password == "ilovepython":
        failed_login = 0
        return "OK"

    if username == "cluett" and password == "matrix":
        failed_login = 0
        return "OK"

    if username == "stangeby" and password == "rigorous":
        failed_login = 0
        return "OK"

    failed_login += 1

    return "Refused"

def initialize():
    global failed_logins
    failed_logins = 0

initialize() # When you import the function, stuff inside the main block won't run, so you can move it oustide the main

if __name__ == "__main__":
    trailing_zeros(20)
    initialize()
    print(login("guerzhoy", "asdfdsaf"))
    print(login("guerzhoy", "asdfds"))
    print(login("guerzhoy", "ilovepython"))
    print(login("guerzhoy", "asdfds"))

# You can import other files to use the functions within it
# Write import filename at the top
# To access the function write filename.function(var,var)
