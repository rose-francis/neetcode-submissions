class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        l_no=0
        r_no=m*n-1

        while l_no <= r_no:
            
            m_no=(l_no+r_no)//2
            m1=m_no//n
            m2= m_no%n

            if target==matrix[m1][m2]:
                return True
            elif target<matrix[m1][m2]:
                r_no=m_no-1
            else:
                l_no=m_no+1

        return False
