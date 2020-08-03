
# def threeSum(self, nums: List[int]) -> List[List[int]]:
import itertools
from collections import OrderedDict 
def treeSum(nums):
    # nums = dict.fromkeys(nums)
    nums.sort()
    # print(nums)
    comb= itertools.combinations(nums,3)
    result = []
    for i in comb:
        # print(i)
        if sum(i)==0:
            if list(i) not in result:           
                result.append(list(i))
   
    # print(result[0])
    # print(result)
    # result.sort()
    return result

# print(treeSum([1,2,3,4,5]))
# output= treeSum([-1,0,1,2,-1,-4])
# print(treeSum([-1,0,1,2,-1,-4]))

# Output=>   [[-1,0,1],[-1,2,-1],[0,1,-1]]
# Expected=> [[-1,-1,2],[-1,0,1]]
# test= [-1,-1,2]
# if test in output: 
#     print("Got it")

def sum3(nums):
    nums.sort()
    cache =[]
    
    for i in range (len(nums)-2):
        left=i+1
        right = len(nums)-1
        
        while left<right:
            sum = nums[i]+nums[left]+nums[right]
            
            if sum == 0:
                cache.append([ nums[i],nums[left],nums[right]])
                left+=1
                right-=1
            elif sum<0:
                left+=1
            else:
                right-=1
     
    result=[]
    print(cache)
    
    for i in cache:
        if i not in result:
            result.append(i)
    return result
      
print(sum3([-1,0,1,2,-1,-4]))

# Output=>   [[-1,0,1],[-1,2,-1],[0,1,-1]]
# Expected=> [[-1,-1,2],[-1,0,1]]


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        cache =[]
        
        for i in range (len(nums)-2):
            if i>0 and nums[i]== nums[i-1]: continue
            
            left=i+1
            right = len(nums)-1
            
            while left<right:
                sum = nums[i]+nums[left]+nums[right]
                
                if sum == 0:
                    cache.append([ nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif sum<0:
                    left+=1
                else:
                    right-=1
        return cache