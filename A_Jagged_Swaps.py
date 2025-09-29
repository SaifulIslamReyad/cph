for _ in range(int(input())):
    n=int(input())
    L=list(map(int, input().split()))
    print("YNEOS"[L[0]!=1::2])
