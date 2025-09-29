for _ in range(int(input())):
    n=int(input())
    L = list(map(int, input().split()))
    LL= sorted(L)
    max= LL[-1]
    max2= LL[-2]
    for i in range(n):
        if L[i]==max: print(max-max2 , end = " ")
        else: print(L[i]-max , end= " ")
    print()
    

    