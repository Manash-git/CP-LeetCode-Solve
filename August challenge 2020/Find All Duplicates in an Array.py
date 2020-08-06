li1= [9,8,4,1,2,2,0,5,5]
# li2= list(set(li1))
# print(li2)

# for i in list(set(li1)):
#     if i in li1:
#         li1.remove(i)
        

nums= sorted(li1)
print(nums)

output=[]
for i in range(1,len(nums)):
    if nums[i]==nums[i-1]:
        output.append(nums[i])
print(output)
# print(li1)