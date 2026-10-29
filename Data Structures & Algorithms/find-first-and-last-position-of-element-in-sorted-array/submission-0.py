class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[-1,-1]
        l=0
        r=len(nums)-1
        first=0
        last=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                first=mid
                last=mid
                while (first-1)>=0 and nums[first-1]==nums[first]:
                    first-=1
                while (last+1)<len(nums) and nums[last+1]==nums[last]:
                    last+=1
                return [first,last]
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        
        return res