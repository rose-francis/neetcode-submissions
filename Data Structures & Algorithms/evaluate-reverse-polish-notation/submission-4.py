class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if i.isdigit():
                stack.append(int(i))
            elif (i[0]=='-' and i[1:].isdigit()):
                stack.append(-int(i[1:]))
            else:
                op2=stack.pop()
                op1=stack.pop()
                if i=='+':
                    res=op1+op2
                elif i=='-':
                    res=op1-op2
                elif i=='*':
                    res=op1*op2
                elif i=='/':
                    res=int(op1/op2)
                stack.append(res)
        res=stack.pop() 
        return res             
                
                