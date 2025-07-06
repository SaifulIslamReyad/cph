for _ in range(int(input())):
    s=input()
    if len(s)<3: print("NO")
    elif s[:2] != "10" : print("NO")
    elif len(s[2:])==1 and int(s[2]) <=1 :  print("NO")
    elif len(s[2:])>=2 and s[2]=="0" : print("NO")
    else: print("YES")