class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicti={}
        n=len(nums)
        for i in range(n):
            num2=target-nums[i]
            if num2 in dicti:
                return [dicti[num2],i]
            dicti[nums[i]]=i
            
            


        