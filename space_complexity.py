def fibo(n):
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        b, a = a + b, b
    return b
print(fibo(6))


def fibo_recursive(n):
    if n < 2:
        return n
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)

print(fibo_recursive(6))


def fibo_iterative(n):
    if n < 2:
        return n
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[-1] + fib[-2]) 
    return fib[n]

print(fibo_iterative(6))  


def fibo_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n < 2:
        return n
    memo[n] = fibo_memo(n - 1, memo) + fibo_memo(n - 2, memo)
    return memo[n]

print(fibo_memo(6))  


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def create_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    return matrix



def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def store_numbers(n):
    arr = []  
    for i in range(n):
        arr.append(i)
    return arr


def sum_two_numbers(a, b):
    return a + b  

def printArray(L):
    for i in L: print(i, end = " ")

printArray([0,1,2,2,2,1])
