#taking input by space
#a, b = map(int, input().split())
#char array
A="hello world"
print(A[0])
print(A[:2])
print(A[-1])
print(A[1:-1])
print(A[-4:])
lllist=["Reyad", 14]
print(lllist)
print(lllist[0])
print(lllist[0][0])
tttuple=("sakib",12)
print(tttuple)
print(tttuple[0])
print(tttuple[0][0])



a="hello"
a[0]="j"  #error
print(a) 
a = "j" + a[1:]
print(a)  # Output will be "jello"
a="jelloooo"
print(a) #Output will be "jelloooo"


L= [[2,3,4],[60,80],[3,4,5]]
print(sorted(L))
# [[2, 3, 4], [3, 4, 5], [60, 80]]