n = 2
print(type(f"{n}"))

for i in range(1,n):
    if "0" not in f"{i}{n-i}":
        # return [i,n-i]
        print(i,n-i)
        break