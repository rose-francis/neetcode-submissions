class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l1=0
        l2=0
        m=len(matrix)
        n=len(matrix[0])
        r1=m-1
        r2=n-1
        while l1<=r1 and l2<=r2:
            mid1=(r1+l1)//2
            mid2=(r2+l2)//2
            if matrix[mid1][mid2]>target:
                if mid2==0:
                    r2=n-1
                    r1=mid1-1
                else:
                    r2=mid2-1
            elif matrix[mid1][mid2]<target:
                if mid2==n-1:
                    l1=mid1+1
                    l2=0
                else:
                    l2=mid2+1
            else:
                return True
        return False
                
            

        
        