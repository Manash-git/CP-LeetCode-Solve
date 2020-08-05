def isValid(s):
    stack=[]
    pairs={
        '(':')',
        '[':']',
        '{':'}'
    }
    
    for char in s:
        if char in pairs:
            # storing corresponding closing parenthesis
            stack.append(pairs[char]) 
            # print(stack)
        
        else:
            if not stack or stack.pop() != char:
                return False
    
    # print("Final=>",stack)
    return not stack        

print(isValid("()[{}]"))
print(isValid("()[]{}"))













# test=[]
test=[1]
# print(not test)  # Return True if list is empty. Bcoz: empty = False. so not False= True
# print(test)