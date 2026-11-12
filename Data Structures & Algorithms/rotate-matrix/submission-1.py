class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        i=0
        j=len(matrix)-1
        while i<j:
            temp=matrix[i]
            matrix[i]=matrix[j]
            matrix[j]=temp
            i+=1
            j-=1
            
        
        for i in range(len(matrix)-1):
            for j in range(1,len(matrix[0])):
                if i<j:
                    temp=matrix[i][j]
                    matrix[i][j]=matrix[j][i]
                    matrix[j][i]=temp
        