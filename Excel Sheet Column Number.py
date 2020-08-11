print(ord("A"))
# print(ord("A")%64)
# print(ord("a"))

s="AA"
s="ZY"
output=0
for c in s:
    temp = ord(c)%64
    output = output *26 + temp
    

print(output)