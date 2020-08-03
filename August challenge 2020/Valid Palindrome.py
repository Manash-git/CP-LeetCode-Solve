sent = "A man, a plan, a canal: Panama"
sent = "".join(i for i in sent if i.isalpha())
# print(sent)

s= "manash"
s= "mam"
# print(s[::-1])
# print(s.find(s[::-1])==0)


# def isPalindrome(self, s: str) -> bool:

def isPalindrome(s):
    s= "".join(i for i in s if i.isalnum())
    print(s)
    s=s.lower()
    
    if s==s[::-1]:
        return True
    else:
        return False 

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
str1="a12BB"
# print(str1.lower())
