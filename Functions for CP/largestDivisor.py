n=100
for i in range(2,int(100**0.5)):
    if n%i==0:
        largest=n//i
        break
print(largest)