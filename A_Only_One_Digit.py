for _ in range(int(input())):
    L= set()
    s=input()
    for i in s:
        L.add(i)
    print(min(L))