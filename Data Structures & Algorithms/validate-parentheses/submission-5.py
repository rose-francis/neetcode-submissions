class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in ['(','[','{']:
                stack.append(i)
            else:
                if not stack:
                    return False
                elif (i==')' and stack[-1]=='(') or (i==']' and stack[-1]=='[') or (i=='}' and stack[-1]=='{'):
                    stack.pop()
                else:
                    return False
            
        return True if not stack else False




