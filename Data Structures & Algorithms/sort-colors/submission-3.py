class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=[0]*3
        for a in nums:
            count[a]+=1
        
        j=0
        for i in range(3):
            for k in range(count[i]):
                nums[j]=i
                j+=1
        

        