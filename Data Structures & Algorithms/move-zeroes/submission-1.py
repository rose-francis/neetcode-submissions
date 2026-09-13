class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=[]
        for i in nums:
            if i!=0:
                n.append(i)
        
        for i in range(len(nums)):
            if i<len(n):
                nums[i]=n[i]
            else:
                nums[i]=0
