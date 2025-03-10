for _ in range(int(input())):
    n = int(input())
    L1, L2, L3 = [list(map(int, input().split())) for _ in range(3)]
    L1 = list(zip(L1, range(n)))
    L2 = list(zip(L2, range(n)))
    L3 = list(zip(L3, range(n)))
    L1.sort(reverse=True)
    L2.sort(reverse=True)
    L3.sort(reverse=True)
    ans = 0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if L1[i][1] != L2[j][1] and L1[i][1] != L3[k][1] and L2[j][1] != L3[k][1]:
                    ans = max(ans, L1[i][0] + L2[j][0] + L3[k][0])
    print(ans)


for _ in range(int(input())):
    n=int(input())
    A,B,C=[list(map(int,input().split()))for i in range(3)]
    A=[(A[i],i)for i in range(n)]
    B=[(B[i],i)for i in range(n)]
    C=[(C[i],i)for i in range(n)]
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)
    ans=0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if A[i][1]==B[j][1] or A[i][1]==C[k][1] or B[j][1]==C[k][1]:continue
                ans=max(ans,A[i][0]+B[j][0]+C[k][0])
    print(ans)