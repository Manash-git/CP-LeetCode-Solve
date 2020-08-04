import math
# math.log(a,Base)
# print(math.log(4,2))
res =math.log2(6)
# print(res)
# print(math.floor((res)))
# print(math.ceil((res)))

def isPowerOfFour(num):
    if num<=0: return False
    
    if math.floor(math.log(num,4))==math.ceil(math.log(num,4)):
        return True
    else:
        return False
    
print(isPowerOfFour(4))
print(isPowerOfFour(0))
print(isPowerOfFour(5))