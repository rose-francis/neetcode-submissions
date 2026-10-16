class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums)==1:
            return 1
        k=0
        for i in range(1,len(nums)):
            if nums[i-1]!=nums[i]:
                nums[k+1]=nums[i]
                k+=1
                
        
        return k+1