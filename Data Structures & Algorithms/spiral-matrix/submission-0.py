class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        m=len(matrix)
        n=len(matrix[0])
        row=[0]*m
        col=[0]*n

        top=0
        right=n-1
        bottom=m-1
        left=0
        t=1
        while True:
            if len(res)==m*n:
                break
            if t%4==1:
                i=top
                for j in range(left,right+1):
                    res.append(matrix[i][j])
                top+=1
            elif t%4==2:
                j=right
                for i in range(top,bottom+1):
                    res.append(matrix[i][j])
                right-=1
            elif t%4==3:
                i=bottom
                for j in range(right,left-1,-1):
                    res.append(matrix[i][j])
                bottom-=1
            else:
                j=left
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][j])
                left+=1
            t+=1
        
        return res

        


