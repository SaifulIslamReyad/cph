def reyad(n):
    if n==1: print(1, end= " ") ; return
    print(n,end= " ")
    if n%2==0 : reyad(n//2)
    else : reyad(n*3 +1)

reyad(int(input()))