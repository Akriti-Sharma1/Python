def fact_while(n):
    current_product = 1
    i = 1
    while i != n+1:
        curent_product += i
        i += 1
    return current_product

def fact_iter(n,cur_prod,i):
    if i == n+1:
        return cur_prod
    return fact_iter(n,cur_prod*i, i+1)

print(fact_iter(4,1,1))

# Default parameters
# def f(x,y=5)
# can call f(2) like you don't need to call with a y value
def fact(n):
    if n <= 1:
        return 1
    return n*fact(n-1)