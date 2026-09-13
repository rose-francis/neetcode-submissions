class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=min(len(nums1), len(nums2))
        i,j=0,0
        nums=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                nums.append(nums1[i])
                i+=1
            else:
                nums.append(nums2[j])
                j+=1
        
        if i<len(nums1):
            nums.extend(nums1[i:])
        
        if j<len(nums2):
            nums.extend(nums2[j:])
        
        if len(nums)%2==0:
            m=len(nums)//2
            median=(nums[m] + nums[m-1])/2
        else:
            median=nums[len(nums)//2]

        return median
