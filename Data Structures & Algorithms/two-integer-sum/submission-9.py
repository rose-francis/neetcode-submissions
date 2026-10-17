class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i,a in enumerate(nums):
            diff=target-a
            if diff in d:
                   return [d[diff], i]
            d[a]=i
        
    