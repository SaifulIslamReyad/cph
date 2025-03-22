# T(n) = O(f(n)) + a * T(n-b)

def sajib(n):
    if n<=0 : return
    print(n*"oi kire")
    sajib(n-1)
    sajib(n-1)

sajib(4)


