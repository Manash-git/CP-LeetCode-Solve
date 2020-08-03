import math

class Solution:
    def myPow(self,x,n):
        if n==0: return 1.0
        if n==1: return x
        
        if n<0:
            return self.myPow(1/x, -n)
        result= self.myPow(x*x, n//2)
        if n%2==1: 
            result*=x
        return result