import math
def isPowerOfThree(n):
    # if n<=0: return False
    
    # if math.floor(math.log(n,3))==math.ceil(math.log(n,3)):
    #     return True
    # else:
    #     return False
    return  0 if n<=0 else 3**math.ceil(math.log(n,3))==n
    
# print(isPowerOfThree(27))
# print(isPowerOfThree(0))
# print(isPowerOfThree(9))
# print(isPowerOfThree(45))
# print(isPowerOfThree(243))
test = math.log(8,3)
print(test)
# print(math.floor(test))
# print(math.ceil(test))
# print(3**math.ceil(test))
# print(math.ceil(.5))
