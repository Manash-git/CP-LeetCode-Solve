def makeGood(s):
    bucket=[s[0]]
    
    for i in s[1:]:
        if bucket and i.lower()==bucket[-1] and i!=bucket[-1]:
            bucket.pop()
        elif bucket and i.upper()==bucket[-1]and i!=bucket  [-1]:
            bucket.pop()
        else:
            bucket.append(i)
    
    print(bucket)  
    # print("".join(bucket))
    return "".join(bucket)

print(makeGood("mannNasSh"))


lst= [1,5,3,7]
print(lst[-1])
        