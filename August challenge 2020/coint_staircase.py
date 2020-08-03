def coin(n):
    if n==0: return 0
    i=1
    while True:
        n=n-i
        if i>=n:
            return i 
        i+=1

print(coin(9))
    