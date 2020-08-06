'''Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].
'''
low = 3 
high = 7
# 800445804
# 979430543
# low = 800445804
# high = 979430543
count=0
for i in range(low,high+1):
    if i%2!=0:
        count+=1

print(count)

def countOdd(low,high):
    total_no= (high-low)+1
    if total_no%2==0:
        return total_no//2
    elif high%2==0 and low%2==0:
        return total_no//2
    else:
        return (total_no//2)+1
    
print(countOdd(3,7))
print(countOdd(800445804,979430543))

