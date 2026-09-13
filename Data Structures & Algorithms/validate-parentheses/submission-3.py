class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        top=-1
        for i in s:
            if i in ['(','[','{']:
                stack.append(i)
                top+=1
            else:
                if top==-1:
                    return False
                elif (i==')' and stack[top]=='(') or (i==']' and stack[top]=='[') or (i=='}' and stack[top]=='{'):
                    stack.pop()
                    top-=1
                else:
                    return False
            
        if top==-1:
            return True
        else:
            return False




