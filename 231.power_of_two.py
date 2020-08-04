import math
def isPowerOfTwo(n):
    if n<=0: return False
    
    if math.floor(math.log2(n)) == math.ceil(math.log2(n)):
        return True
    else:
        return False
    
# print(isPowerOfTwo(4))
# print(isPowerOfTwo(0))
# print(isPowerOfTwo(5))
# print(isPowerOfTwo(1))
print(isPowerOfTwo(536870912))
# print(math.log(536870912,2))
# print(math.log2(536870912))