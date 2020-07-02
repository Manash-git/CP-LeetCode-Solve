class Solution:
    # Hash Map solution
    
    def twoSum(self, nums, target):
        compliment=dict()
        res=[]
        for index,value in enumerate(nums):
            if compliment.get(value) is None:
                compliment[target-value]=index
            else:
                res =[compliment[value],index]
                
        # print(compliment)
        return res

l=Solution()
print(l.twoSum([2, 7, 11, 15],17))

'''
# BruteForce solution

def twoSum(self, nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            # print("I,j=>",i,j)
            # print("Value=> ",nums[i],nums[j])
            # print("Sum => ",nums[i]+nums[j])
            # if nums[i]+nums[j]
            # print()
            if nums[i]+nums[j]== target:
                return [i,j]
                # return [nums[i],nums[j]]
                
    return []
'''

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1]
