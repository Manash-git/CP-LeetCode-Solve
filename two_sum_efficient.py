class Solution:
    def twoSum(self, nums, target):
        lst=nums[:]
        lst.sort()
        # print(nums)
        # print(lst)
        # print()
        i=0
        j=len(nums)-1
        # res=[]
        # print(i,j)
        # print(nums[i]+nums[j])
        
        while i<=j:
            if (lst[i]+lst[j]) == target:
                # print(lst[i],lst[j])
                # print(nums.index(lst[i]),nums.index(lst[j]))
                # return [nums.index(lst[i]),nums.index(lst[j])]
                # return [i,j]
                
                if lst[i]==lst[j]:
                    return [nums.index(lst[i]),nums.index(lst[j],nums.index(lst[i])+1)]
                else:
                    return [nums.index(lst[i]),nums.index(lst[j])]
            else:
                if (lst[i]+lst[j]) < target:
                    i=i+1
                else:
                    j=j-1
        # print(res)
        return []
    

l1=[3,2,4]
# print(l1.index(4))

l=Solution()
# print(l.twoSum([2, 7, 11, 15],16))
# print(l.twoSum([3,2,4],6))
print(l.twoSum([3,3],6))
# print(res)
