# map(int, input().split())
# প্রথমে ফাংশন পরে আইটারেট করা যায় এমন
l= [1,2,3,4,5]
def square(x):
    return x*x
s= list(map(square,l))
ss= list(map(lambda x: x*x,l))


a=[1,2,3,4]
b=[4,3,2,1]
# to add b

c= list(map(lambda n,m: n+m  , a,b ))
print(c)