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


L = [[2,3,4],[60,80],[3,4,5]]
# sort by length (shorter sublists first)
print(sorted(L, key=len))  # [[60, 80], [2, 3, 4], [3, 4, 5]]





data = [[1, 3], [1, 2], [2, 1]]
# Sort first by first element, then by second element
data.sort(key=lambda x: (x[0], x[1]))
print(data)
# Output: [[1, 2], [1, 3], [2, 1]]









data = [[3, 2], [1, 4], [2, 3]]

# Sort by second element
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)

data = [[3, 2], [1, 4], [2, 3]]

# Sort in place by first element
data.sort(key=lambda x: x[0])
print(data)