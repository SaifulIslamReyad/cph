def factorial(n):
    if n==1 or n==0 : return 1
    return n* factorial(n-1)
print(factorial(5))

def print_nTO1(n):
    if n==1: return [1]
    L=[n]+ print_nTO1(n-1)
    return L
print(print_nTO1(5))

def print_n_to_1(n):
    if n==1:print(n); return
    print_n_to_1(n-1)
    print(n)
    return
print_n_to_1(5)

def print_1_to_n(n):
    print(n)
    if n==1: return
    print_1_to_n(n-1)
print_1_to_n(6)

def pattern(n):
    print(n*'*')
    if n==1: return
    pattern(n-1)
pattern(5)

def pattern_rev(n):
    if n==1: print("*") ; return
    pattern_rev(n-1)
    print(n*"*")
pattern_rev(5)

def check(n):
    c= False
    if n==0: c= True
    while n>0:
        n/=2
        if n==1 : c= True
    return c
print(check(32))

def check_recur(n):
    if n==1 or n==0: return True
    if round(n)==0: return False
    y= False or check_recur(n/2)
    return y
print(check_recur(3))

def sumTo1(n):
    if n==0: return 0
    return n+ sumTo1(n-1)
print(sumTo1(4))

def nthFibo(n):
    if n==1 : return 0
    if n==2: return 1
    return nthFibo(n-1)+ nthFibo(n-2)
print(nthFibo(9))

def makeListfromNto1(n):
    if n==0: return []
    return [n] + makeListfromNto1(n-1) 
print(*makeListfromNto1(int(input())))

def printNumbersFromNo1(n):
    print(n , end = " ")
    if n>1: printNumbersFromNo1(n-1)

def fib(n):
    if n<=2: return n-1
    return fib(n-1)+ fib(n-2)
print(fib(int(input())))