def removeElement(nums):
    n= len(nums)
    if n== 0 or n==1: return n
    # count=0
    # for i in range(1,len(nums)):
      
    #     if nums[i]==nums[i-1]:
    #         count+=1
    # print(count)
    # print(len(nums)-count)
    temp= nums[0]
    for i in nums[1:]:
        if i == temp:
            nums.remove(i)
        else:
            temp=i
           
    return len(nums)
        
    # return len(nums)
removeElement([1,2,2,4,4,9,12,12])
# print(len([1,2,2,4,4,9,12]))

lst=[1,2,3,4,5,6]
# print(lst[1:])