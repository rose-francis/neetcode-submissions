class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        s=0
        for n in nums:
            s=s^n
        return s