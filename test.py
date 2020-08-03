import itertools

data = [3,1,2,5,4]
# data = [-1,0,1,2,-1,-4]
# print(list(set(data)))
# print(itertools.permutations(data))

# result = itertools.permutations(data)
result = itertools.combinations((data),3)
# print(result)
# print(list(result))

output = []
for i in result:
    # print(i[0],i[1],i[2])
    # print(list(i))
    # print("Sum=> ",sum(i))
    if sum(i)==10:
        output.append(list(i))

print("Final=> ", output)
# output[0].sort()
# print("Final=> ", output[0])
if 