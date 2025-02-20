def kadanesAlgorithm(array):
    maxEndingHere = array[0]
    maxSoFar = array[0]
    for num in array[1:]:
        maxEndingHere = max(num, maxEndingHere + num)
        maxSoFar = max(maxSoFar, maxEndingHere)
    return maxSoFar
print(kadanesAlgorithm([3, 5, -2, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4])) # 25



def kadane_algo_2(L):
    ans = L[0]
    sum = 0
    for i in L: 
        sum += i
        ans = max(sum,ans)
        if sum<0: sum = 0
    return ans
print(kadane_algo_2([3, 5, -2, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4])) # 25


