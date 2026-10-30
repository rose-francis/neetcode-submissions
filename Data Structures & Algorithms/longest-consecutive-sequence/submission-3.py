class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        maxC=0
        for a in s:
            if (a-1) not in s:
                c=0
                while a in s:
                    c+=1
                    a+=1
                maxC=max(c,maxC)
        return maxC