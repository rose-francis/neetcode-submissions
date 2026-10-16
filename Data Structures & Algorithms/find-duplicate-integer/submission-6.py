class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=0
        fast=0
        while slow<len(nums) and fast<len(nums):
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                s2=0
                while slow!=s2:
                    slow=nums[slow]
                    s2=nums[s2]
                return slow
        