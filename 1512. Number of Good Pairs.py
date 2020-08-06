nums = [1,2,3,1,1,3]
nums = [1,1,1,1]
# nums = [1,2,3]
count=0

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        # print(nums[i],nums[j])
        if nums[i] == nums[j]:
            count+=1
print(count)