def factorial(n):
    if n==1 or n==0 : return 1
    return n* factorial(n-1)

def print_nTO1(n):
    if n==1: return [1]
    L=[n]+ print_nTO1(n-1)
    return L

def print_1_to_n(n):
    if n==1:print(n); return
    print_1_to_n(n-1)
    print(n)
    return


def print_n_to_1(n):
    print(n)
    if n==1: return
    print_n_to_1(n-1)

def pattern(n):
    print(n*'*')
    if n==1: return
    pattern(n-1)

def pattern_rev(n):
    if n==1: print("*") ; return
    pattern_rev(n-1)
    print(n*"*")

def check(n):
    c= False
    if n==0: c= True
    while n>0:
        n/=2
        if n==1 : c= True
    return c

def check_recur(n):
    if n==1 or n==0: return True
    if round(n)==0: return False
    y= False or check_recur(n/2)
    return y

def sumTo1(n):
    if n==0: return 0
    return n+ sumTo1(n-1)

def nthFibo(n):
    if n==1 : return 0
    if n==2: return 1
    return nthFibo(n-1)+ nthFibo(n-2)

def makeListfromNto1(n):
    if n==0: return []
    return [n] + makeListfromNto1(n-1) 

def printNumbersFromNo1(n):
    print(n , end = " ")
    if n>1: printNumbersFromNo1(n-1)

def fib(n):
    if n<=2: return n-1
    return fib(n-1)+ fib(n-2)
