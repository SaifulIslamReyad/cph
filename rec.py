def rec(n):
    if n==0: return []
    return [n] + rec(n-1) 
print(*rec(int(input())))
    