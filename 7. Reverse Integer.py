class Solution:
    def reverse(self, x):
        # res=0
        # if x<((2**31)-1) and x> -(2**(31)):
        #     if x>=0:
                
        #         # print(int(str(x)[::-1]))
        #         # print(type(int(str(x)[::-1])))
        #         return int(str(x)[::-1])
        #     else:
        #         pos=-1*x
        #         pos=-1*(int(str(pos)[::-1]))
        #         return pos
        # else:
        #     return 0  
        
        
       
        if x>=0:
                
            # print(int(str(x)[::-1]))
            # print(type(int(str(x)[::-1])))
            res=int(str(x)[::-1])
        else:
            res=-1*x
            res=-1*(int(str(res)[::-1]))
        
        if res<((2**31)-1) and res> -(2**(31)):
            return res
        else:
            return 0   
       
        
            
l=Solution()
print(l.reverse(253))
print(l.reverse(-123))
print(l.reverse(120))
print(l.reverse(1534236469))

# print((2**31)-1)
# print(-(2**31))
