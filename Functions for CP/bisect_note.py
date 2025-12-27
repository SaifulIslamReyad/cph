import bisect

ascending_list = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,9,9]

print(bisect.bisect_left(ascending_list, 5))     
print(bisect.bisect_right(ascending_list, 8))   
bisect.insort_left(ascending_list, 8)  
bisect.insort_right(ascending_list, 6)  

def bisect_descendingList(L,value,direction="left"):
    L=list(map(lambda x: -x , L))
    value *= -1
    return bisect.bisect_left(L,value) if direction=="left" else bisect.bisect_right(L,value)


descending_list= [9,9,9,5,4,4,3,3,2,1,1,1,1]
print(bisect_descendingList(descending_list,4,"left"))
print(bisect_descendingList(descending_list,4,"right"))
