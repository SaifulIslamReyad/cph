a=["apple","banana",50,2.5,[1,2,3,4,"Reyad"]]
print(a)
print(a[4])
print(a[0][0])
print(a[4][4][4])
print(a[-1][-1][-1])
print(a[0:-2])
b,c,d,*e=a # after b,c,d rest of the elements will be in list e
# but we cannot do *l=map(int, input().split())
# l=list(map(int, input().split()))
print(b)
print(c)
print(d)
print(e)
a.append(100)
print(a)
a.append([1,2,3,4])
print(a)
x=[1,2,3,4]
a.extend(x)
print(a)
a.insert(0,"jackfruit")
a.insert(4,"banana")
a.remove("banana")
print(a)
a.pop() #removes last element
a.pop(1) #index
a.clear() #clears the list
print(type(a))
x=[12,1,2,3,6,1]
x.sort() #increasing
print(x)
x.sort(reverse=True) #decreasing
print(x)
y=["a","b","f","c"]
y.sort() #lexi
print(y)
z=["apple","abba","zoo","banana"]
z.sort()
print(z)
z.reverse()
print(z)


L= [[2,3,4],[60,80],[3,4,5]]
print(sorted(L))
# [[2, 3, 4], [3, 4, 5], [60, 80]]