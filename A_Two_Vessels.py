import math as m
for _ in range(int(input())):
    a,b,c = map(int, input().split())
    print(m.ceil(abs(a-b)/(2*c)))