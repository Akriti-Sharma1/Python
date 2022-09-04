import math

# Problem 1
def sum_nums(L):
    s = 0
    for num in L:
        s += num

    return s

def count_evens(L):
    counter = 0
    for i in L:
        if i % 2 == 0:
            counter += 1

    return counter

def list_to_str(lis):
    counter = []
    for i in range(0, len(lis)):
        new = str(lis[i])
        counter.append(new)

    return counter

def lists_are_the_same(list1, list2):
    counter = 0
    if len(list1) == len(list2):
        for i in list1:
            if list1[i] != list2[i]:
                return False
            return True
    return False

def simplify_fraction(n, d):
    i = 2
    while i < min(n, d) + 1:
        if n % i == 0 and d % i == 0:
            n = n // i
            d = d // i
        else:
            i += 1
    return n, d

def pi():
    ''' Returns the approximation of pi using the Leibniz formula
    which is: the consecutive sum of (-1^n)/(2n+1)
    >>> pi()
    >>> 3.99
    '''
    counter = 0 # Counter for intermediate values
    counter2 = 0
    for n in range(0, 1001): # Iterates through numbers from 0 to 1000
        num = (-1)**n # Calculates the numerator of the formula
        denom = (2*n) + 1 # Calculates the denominator of the formula
        real = num / denom # Calculates the final answer
        counter += real # Adds the final answer to counter
        counter2 += 1

    return 4 * counter, counter2 # Multiplied by 4 to get the approximation of pi

x = math.pi
def check_digits():
    counter = 0
    pi_approx = str(x*(10**300))
    for i in str(pi()):
        for j in pi_approx:
            if i == j:
                counter += 1
    return counter


if __name__ == "__main__":
    print(check_digits())
    #print(list_to_str([1,2,3,4,5,6,7]))
    print(lists_are_the_same([1,2,3], [1,2,3]))
#     print(simplify_fraction(4,6))

    #print(pi())


