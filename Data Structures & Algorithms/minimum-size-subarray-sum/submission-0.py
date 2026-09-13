class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res=float("infinity")
        l=0
        total=0
        for r in range(len(nums)):
            total+=nums[r]
    
            while total>=target:
                if r-l+1<res:
                    res=r-l+1
                total-=nums[l]
                l+=1

        return res if res!=float("infinity") else 0
                
