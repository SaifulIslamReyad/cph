n= 100
for i in range(1,n+1):
    c=0
    for j in range(1,i+1):
        c^=j
    print(f"for {i=} ,{c= }") 