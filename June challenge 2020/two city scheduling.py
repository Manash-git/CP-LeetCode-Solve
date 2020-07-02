# Input: [[10,20],[30,200],[400,50],[30,20]]
# Output: 110

costs= [[10,20],[30,200],[400,50],[30,20]]

refund = []
N = len(costs)//2
# print(N)
minCost = 0
for A, B in costs:
    refund.append(B - A)
    minCost += A

# print(refund)
refund.sort()
# print(refund)

for i in range(N):
    minCost += refund[i]
# return minCost

# print(minCost)

FirstCity = [i for i,j in costs]
# print(FirstCity)
Diff = [j - i for i,j in costs]
# print(sorted(Diff)[:len(costs)//2])
# print(Diff)
# print(sorted(Diff))
# print(Diff[:len(costs)//2])
# print(Diff)
# return sum(FirstCity) + sum(sorted(Diff)[:len(costs)//2])
# print(sum(FirstCity))
# print(sum(FirstCity) + sum(sorted(Diff)[:len(costs)//2]))

# return sum([i for i, j in costs]) + sum(sorted([j - i for i,j in costs])[:len(costs)//2])


# My solution

t_cost= sum([i for i,j in costs])
# print(t_cost)
# diff_list= [j-i for i,j in costs]
# print(diff_list)
# diff_list.sort()
# diff_list=diff_list[:len(costs)//2]
# # diff_list.sort()[:2]
# print(diff_list)
# t_cost= t_cost + sum()

refund = sum(sorted([j-i for i,j in costs])[:len(costs)//2])
# print(refund)

# print(t_cost+ refund)

def twoCitySchedCost(self, costs):
    t_cost= sum([i for i,j in costs])
    refund = sum(sorted([j-i for i,j in costs])[:len(costs)//2])
    return t_cost+refund

print(twoCitySchedCost(1,costs))