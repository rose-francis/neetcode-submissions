class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        right=m*n-1
        left=0
        while left<=right:
            mid=(left+right)//2
            m1=mid//n
            m2=mid%n
            if target==matrix[m1][m2]:
                return True
            elif target>matrix[m1][m2]:
                left=mid+1
            else:
                right=mid-1
        return False

        