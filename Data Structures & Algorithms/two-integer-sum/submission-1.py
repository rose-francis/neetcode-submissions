class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            e=target-nums[i]
            if e in nums and nums.index(e)!=i:
                if i<nums.index(e):
                    return [i,nums.index(e)]
                else:
                    return [nums.index(e),i]