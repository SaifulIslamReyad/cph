def maxSumNonAdjacent(d):
    a=b=0
    for i in d:
        a,b=max(a,i+b),a
    return a
print(maxSumNonAdjacent([4,1,1,2,1,1,2,4,1,2,2,2,3]))


def HouseRob1(nums):
    if len(nums)<3: return(max(nums))
    nums[2]= nums[0]+nums[2]
    for i in range(3,len(nums)):
        nums[i]+= max(nums[i-3], nums[i-2])
    return(max(nums[-1],nums[-2]))

def houseRobTwo(nums):
    if len(nums) < 3:
        return max(nums)
    def rob(nums):
        if len(nums) < 3:
            return max(nums)
        nums[2] = nums[0] + nums[2]
        for i in range(3, len(nums)):
            nums[i] += max(nums[i - 3], nums[i - 2])
        return max(nums[-1], nums[-2])
    return max(rob(nums[1:]), rob(nums[:-1]))

