for _ in range(int(input())):
    n,a,b = map(int, input().split())
    s=""
    i=0
    while i < b:
        s+=chr(97+i)
        i+=1
    s+=(a-b)*chr(i+97-1)
    ss=(s*((n//b)+1))[:n]
    print(ss)

    
