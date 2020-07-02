
# strs= ["aab","aaba","baa"]

def longestCommonPrefix(strs):
    result=""
    if len(strs)!=0:
        strs.sort()
        # print(strs)
        first=strs[0]
        # print(first) 
        last= strs[len(strs)-1]
        
        i=0
        str_len=len(min(first,last,key=len))
        # print(str_len)
        while i< str_len:
            if (first[i] != last[i]):
                break
            else:
                result=result+first[i]
            i=i+1
            
    return result

        
    
        
      
    # print(min(first,last,key=len))
    # print(last)


# strs= ["flower","flow","flight"]
strs=[]
# strs= ["dog","racecar","car"]
# strs= ["geeksforgeeks", "geeks", "geek", "geezer"] 
output=longestCommonPrefix(strs)
print(output)