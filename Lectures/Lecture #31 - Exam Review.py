## Recursive Functions
# x^n = x*x^(n-1)
# power(x, n) == x * power(x, n-1)
def power(x,n):
    ''' Return x^n'''
    if n == 0:
        return 1.0
    elif n == 1.0:
        return x
    else:
        return x * power(x, n-1)
#print(power(2,4))

# power(x,0)\
#   ...     /
#   .....
# power(x, n-1) \
#       |       / x^(n-1)
# power(x,n)

#

def power_recursive(x,n):
    xs = []
    while n != 0:
        xs.append(x)
        n -= 1
    power_ret = 1.0
    while len(xs) > 0:
        power_ret = xs.pop() * power_ret
    return power_ret

def power_int(x, n):
    ''' Return x^n
    x is an int
    n >= 0 and an integer'''
    if n == 0:
        return 1
    return x * power(x, n-1)

# x*y takes time O(log(x)* log(y))

# power(x,0)\                   k*log(x)^2*0
#   ...     /
#   .....
# power(x, n-1) \               k*log(x)^2*(n-2)
#       |       / x^(n-1)       k*log(x)^2*(n-1)
# power(x,n)        k * log(x)* log(x^(n-1)) = k*log(x)^2*(n-1)

# Total Runtime = k*log(x)^2*(0+1+2...+(n-1)) = k * log(x)^2*(0+1+2...+(n-1))
                                             #= k * log(x)^2*(n*(n-1)/2)
                                             # is O(log(x)^2n^2)
# r^3 +...+ r^n = (1+r+r^2+...+r^n)-(1+r+r^2)

def factorial(n):
    if n == 0:
        return 1.0

    return n * fact(n-1)

# fact(0)\
#   ...  /1
#   .....
# fact(n-1) \
#   |       / (n-1)!
# fact(n)

def fact_recursive(x,n):
    ns = []
    while n != 0:
        ns.append(x)
        n -= 1
    fact_ret = 1.0
    while len(ns) > 0:
        fact_ret = ns.pop() * power_ret
    return fact_ret



#print(power_recursive(2,4))