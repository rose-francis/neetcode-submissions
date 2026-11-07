class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s=0
        for i in range(1,len(nums)+1):
            s=s^i
        
        e=0
        for n in nums:
            e=e^n
        
        return e^s