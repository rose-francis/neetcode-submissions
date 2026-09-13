class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total=len(nums1) + len(nums2)
        half=total//2
        A,B=nums1,nums2
        if len(B)<len(A):
            A,B=B,A
        
        l=0
        r=len(A)-1
        while True:
            i=(l+r)//2
            j=half -(i+1) -1

            Aleft=A[i] if i>=0 else float("-infinity")
            Aright=A[i+1] if (i+1)<len(A) else float("infinity")

            Bleft=B[j] if j>=0 else float("-infinity")
            Bright=B[j+1] if (j+1) <len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total%2==0:
                    return (max(Aleft,Bleft) + min(Bright, Aright))/2
                return min(Bright,Aright)
            
            elif Aleft>Bright:
                r=i-1
            
            elif Bleft>Aright:
                l=i+1

       

