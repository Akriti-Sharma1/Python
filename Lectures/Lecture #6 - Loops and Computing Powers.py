# Loops and Computing Powers

# for <i> in range (<N>):
#     <block of code>

for i in range(5):
    print(i)
    print(2 * i)
    print("================")

for i in range(100):
    print("I am telling you for the ", i, "th time, EngSci rocks", sep = "")

# a^n = a * a * a * ... * a (n times)
# res = 1
# res = res * a (n times)

def my_pow(a, n):
    '''Compute a^n
    Assume n is a non-negative integer'''

    res = 1
    # res = a^i
    for i in range(n):
        res = res * a

    return res

# While Loops
# while <COND>:
#     <block>
# repeats <block> while <COND> is True

i = 0
while i < 10:
    print(i)
    i = i + 1

print("HI")

# log10(n)
# 10^a = n, find a
# 10^0, 10^1, 10^2 ... 10^a = n

# n = 1000
# res = 1, res = 10^0
# i = 1
def my_log10(n):
    ''' Return log10(n), assume log10(n) is a whole number.'''

    res = 1 # res = 10^i
    i = 0
    while res < n:
        res = res * 10
        i = i + 1

    return i

# Example 2:
def is_prime(n):
    '''Return True iff the non-negative integer n is prime'''

    if n<=1:
        return False
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3,n,2):
        if n % 1 == 0:
            return False

    return True
#7 % 2 = 1 (because 7 = 2*3 + 1)
# 15 % 3 = 0 (because 15 = 5*3 + 0)

# Example 3
#for i in range(start, stop, step)
for i in range(5,17,2):
    print(i)

# continue
for i in range(15, -5, -3):
    if i == 9:
        continue # goes to the next iteration
    print(i)

# break
for i in range(15,-5,3):
    if i == 9:
        break
    print(i)

print("hi")

# pass (uncommon to write)
if a > 5:
    pass # just passes through the function
else:
    print("a is not greater than 5")


if __name__ == '__main__':
    print(my_log10(54))
    print(is_prime(4))

























