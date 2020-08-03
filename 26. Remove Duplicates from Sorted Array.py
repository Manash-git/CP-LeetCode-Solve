def removeElement(nums):
    if len(nums)== 0: return 0
    count=0
    for i in range(1,len(nums)):
      
        if nums[i]==nums[i-1]:
            count+=1
    print(count)
    print(len(nums)-count)
           
    # print(nums)  
        
    # return len(nums)
removeElement([1,2,2,4,4,9,12,12])
# print(len([1,2,2,4,4,9,12]))