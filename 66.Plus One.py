"""
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
"""

input= [1,2,3]
res = "".join(map(str,input))
res = int(res)+1
res = list(map(int,str(res)))

print(res)
# print(type(res))
# print(int(res)+1)