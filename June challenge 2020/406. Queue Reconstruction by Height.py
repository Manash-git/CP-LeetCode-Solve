'''
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''

'''
Algorithm:
step1 :Arrange all the person based on the heights sorted in decreasing order and if two or more person has same heights then compare their K values in assending order.
Step 2: Check according to index = K and insert smallest h before it

Sorted based on height
[[7,0], [7,1], [6,1], [5,0], [5,2], [4,4]]
Now we construct the queue using the sorted person list .
1. Add [7, 0] at 0 --> [[7,0]]
2. Add [7, 1] at 1 --> [[7,0], [7,1]]
3. Add [6, 1] at 1 --> [[7,0], [6,1], [7,1]]
4. Add  [5,0] at 0 --> [[5,0], [7,0], [6, 1], [7,1]]
5. Add [5, 2] at 2 --> [[5,0], [7,0], [5, 2], [6, 1], [7,1]]
6. Add [4, 4] at 4 --> [[5,0], [7,0], [5, 2], [6, 1],[4, 4], [7,1]] which is output
s = sorted(people, key=lambda x: (-x[0], x[1]))

	for i in range(len(s)):
		s.insert(s[i][1], s.pop(i))
'''

# def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

# people.sort(reverse=True)

people.sort(key=lambda x: (-x[0],x[1]))
# res=people
# print(res[0])
# print(res[0][1])
print(people)
# print(res.pop(2))
# print(people)
print()
# res=[]

for i in range(len(people)):
	# print(people)
	# print(i)
    people.insert(people[i][1],people.pop(i))

# for i,sub_list in enumerate(people):
#     people.insert(people[i][1],people.pop(i))
#     print(i,people)

# print("\nResult=> ",people)
    