'''
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Input: haystack = "hello", needle = "ll"
Output: 2
Input: haystack = "aaaaa", needle = "bba"
Output: -1
'''

def strStr(haystack, needle):
    return haystack.find(needle)

print(strStr("hello","ll"))
print(strStr("aaaaa","bba"))
