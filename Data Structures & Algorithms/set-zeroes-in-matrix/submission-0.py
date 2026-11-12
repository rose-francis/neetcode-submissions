class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m=len(matrix)
        n=len(matrix[0])
        row=[-1]*m
        col=[-1]*n

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row[i]=1
                    col[j]=1
        
        for i in range(m):
            if row[i]==1:
                for j in range(n):
                    matrix[i][j]=0
        
        for j in range(n):
            if col[j]==1:
                for i in range(m):
                    matrix[i][j]=0
        
        

        