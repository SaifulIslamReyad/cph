for _ in range(int(input())):
    n, k = map(int, input().split())
    binary_str = bin(k)[2:]
    L=[]
    for i in range(len(binary_str)):
        if binary_str[i] == '0':
            L.append(i)
    LL= []
    x= 0
    while n>0:
        binary_str = bin(x)[2:]
        for i in L:
            if len(binary_str) > i and binary_str[i] == '0': LL.append(x) ; n-=1
            else:break

        x+=1
    print(*LL)