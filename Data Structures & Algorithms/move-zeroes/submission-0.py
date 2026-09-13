class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=[]
        for i in nums:
            if i!=0:
                n.append(i)
        
        i=0
        while i<len(n):
            nums[i]=n[i]
            i+=1
        
        while i<len(nums):
            nums[i]=0
            i+=1
