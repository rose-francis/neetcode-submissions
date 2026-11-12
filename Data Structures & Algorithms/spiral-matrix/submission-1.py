class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        m=len(matrix)
        n=len(matrix[0])

        top=0
        right=n-1
        bottom=m-1
        left=0
        t=1
        while True:
            if len(res)==m*n:
                break
            if t%4==1:
                for j in range(left,right+1):
                    res.append(matrix[top][j])
                top+=1
            elif t%4==2:
                for i in range(top,bottom+1):
                    res.append(matrix[i][right])
                right-=1
            elif t%4==3:
                for j in range(right,left-1,-1):
                    res.append(matrix[bottom][j])
                bottom-=1
            else:
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][left])
                left+=1
            t+=1
        
        return res

        


