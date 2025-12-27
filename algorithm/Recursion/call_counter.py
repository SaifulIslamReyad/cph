def reyad(n, counter ,L):
    if n == 0: print("done") ; return
    L.append(n) ; counter[0] += 1
    reyad(n-1, counter, L)

counter= [0]
L=[]
reyad(5, counter, L)
print("so the total count is ",counter[0])
print(*L)


# pass by reference
