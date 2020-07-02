'''

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

def romanToInt(self, s: str) -> int:
'''

# d= {
#     1:"I",
#     5:"V",
#     10:"X",
#     50:"L",
#     100:"C",
#     500:"D",
#     1000:"M" 
# }
# # print(list(d.keys())[list(d.values()).index("X")])
# # a= list(d.keys())[list(d.values()).index("X")]
# # b= list(d.keys())[list(d.values()).index("M")]
# # print(a+b)
# key= list(d.keys())
# val= list(d.values())
# # print(key[val.index("M")])
# # print(val.index("M"))

# s="XIV" # 14
# sum=0
# for i,value in enumerate(s[::-1]):
#     # print(i,value)
#     if i==0:
#         # print("test")
#         sum= sum+ key[val.index(value)]
#     else:
#         pass
#         # print("\nvalue=> ",value)
#         # if val.index(value)
# # print("\nSum=> ",sum)
    
    
    
    
# # lst= d.keys()
# # print(lst)

# # # s= VIX
# d={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
# s=s[::-1]
# print(s)
# state=0
# big=0
# total=0
# for x in s:
#     print("d[x]=> ",x,d[x])
#     if state==0:
#         state=1
#         total+=d[x]
#         big=d[x]
#         print("#",total,big)
#     else:
#         if d[x]>=big:
#             total+=d[x]
#             big=d[x]
#             print("*",total,big)
#         else:
#             # print("$",big,total)
#             total-=d[x]
#             print("$",total,big)
#     # return total
# print(total)

# def romanToInt(self, s: str) -> int:
s="IXIV" # 13

hash_map= {
    "I":1,
    "V":5, 
    "X":10, 
    "L":50, 
    "C":100, 
    "D":500, 
    "M":1000
}
sum=state=0

for i,value in enumerate(s[::-1]):
    # pass
    if i==0 : 
        sum+= hash_map[value]
        state= hash_map[value]
    else:
        if hash_map[value] >= state:
            sum+= hash_map[value]
            state= hash_map[value]
        else:
            sum-= hash_map[value]
                
return sum
        
print(sum)