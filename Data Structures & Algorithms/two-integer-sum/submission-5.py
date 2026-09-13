class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            n2=target-nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]==n2:
                    return [i,j]
            