class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicti={}

        for i,n in enumerate(nums):
            n2=target-n
            if n2 in dicti:
                return [dicti[n2],i]
            dicti[n]=i

        
            