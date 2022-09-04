# Variable names:

asdfghjkl = 2 # legal
num_coffee_cups = 0 # Porthole case (recommended)  #numCofeeCups
ncc = 2 # legal but not recommended
x = 2 # Usual in beginner (rarely justifiable)

# import math, math.pi
PI = 3.14159265 # Constant in capitals
PI = PI * 1.0000001

N_COURSES = 6

# Loops:
# while True:
#     print("Praxis!") # ctrl + i to stop

# Shell postmortem --> Sends you to the place where the code was stopped by you --> Shell --> Postmortem Debug

# break and continue

# while True:
#     if is_prime(i):
#         break # breaks out of the loop
#     print("Just tried", i)
#     i +=2 # uses the function from before

def find_large_even_prime():
    i = 2
    while True:
        if is_prime(i):
            return i
        i +=2

ENGSCI_IS_FUN = True
if ENGSCI_IS_FUN:
    print("Wheee")

while ENGSCI_IS_FUN: # Not normal convention
    print("Wheee")
    break

# for i in range(n-2):
#     if(i+2) > 2 and i % 2 == 0:
#         continue
#     if n % (2+i) == 0:
#         return False

# The missing k problem

# A list contains the numbers 1, ..., n, in some order, except k is missing
# Determine k without going over the list multiple times

def missing_k(L):
    for i in range(1,len(L)+1):
        if i not in L:
            return i

# Nested Loops:
N = 5
counter = 0
for i in range(3):
    for j in range(2):
        counter += 1
        print(i,j,counter)

if __name__ == "__main__":
    print(missing_k([1,2,3,5,6,7]))




