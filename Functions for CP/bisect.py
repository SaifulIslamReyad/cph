import bisect

sorted_list = [1,1,2,2 ,3,3,4,4,5, 5,6,6, 7,7,9, 9]

print(bisect.bisect_left(sorted_list, 5))  
print(bisect.bisect_left(sorted_list, 8))   
print(bisect.bisect_right(sorted_list, 5))   
print(bisect.bisect_right(sorted_list, 8))   
print()
bisect.insort_left(sorted_list, 6)  
print(sorted_list)  
bisect.insort_left(sorted_list, 8)  
print( sorted_list)  
print()
bisect.insort_right(sorted_list, 6)  
print(sorted_list)  
bisect.insort_right(sorted_list, 8)  
print( sorted_list) 