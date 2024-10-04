#WINDOW MOVE RIGHT


# //SUM OF SUB ARRAY
arr=[1,2,3,4,5,6,7,7,8,9,2,423,234,234,2,34,234,1,23,123,12,4,234]
# to find the minimum sum of subArray of 5 elements we should not do repeatative work 
# any number should not be counted twice 
# to do so we have to add a new number and remove the last from sum 
minimumSum=9999999
sum = sum(arr[0:5])
minimumSum=min(sum,minimumSum)
for i in range (len(arr)-5):
    sum+=arr[i+5]
    sum-=arr[i]
    minimumSum=min(sum,minimumSum)
print(minimumSum)

# //identify
# //continious WindowsError
# //subarray 
# //largest window, minimum sum,maximum sum
# ///variable size window , constant size window









# ///FIRST NEG NUMBER FROM WINDOW 
l= [-1,1, -3,1, -4,2,2,2, -5, -6, -7, 0, 0]
f=0
for i in range(len(l)-2):
    for j in l[i:i+3]:
        if j<0:
            print(j)
            f=1
            break
    if f==0:print(0)
    f=0
