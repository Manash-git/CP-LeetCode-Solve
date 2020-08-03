"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
"""
str1= "ABcd"
# print(str1)
# print(str1[1:])
# print(str1.isupper())
# print(str1[0])
# print(str1[0].isupper())

def capital(word):
    if word.isupper() == True:
        return True
    if word.islower()== True:
        return True
      
    if word[0].isupper() == True:
        word = word[1:]
        if word.islower()==True:
            return True
        else:
            return False
            
print(capital("abc"))          
print(capital("Abc"))          
print(capital("AbcD"))          
print(capital("ABCD"))          
print(capital("g"))          
    



import re


def detectCapitalUse(word):
    return re.fullmatch(r"[A-Z]*|.[a-z]*", word)
print(detectCapitalUse("abc"))