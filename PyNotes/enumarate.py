from icecream import ic

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    ic(index, fruit)


# also works for 2D list
L= [[1,'a'], [ 2, 'b'] , [ 4 , 'd']]
for i,j in L:
    ic(i,j)