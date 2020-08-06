n= 512
n= 234
n= 4421

n=str(n)
add =0
mul =1
res=0
for i in n:
    print(int(i))
    i= int(i)
    mul= mul *i
    add=add + i
res= mul -add
    
print(add)
print(mul)
print(res)