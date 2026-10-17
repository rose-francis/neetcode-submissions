class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i,a in enumerate(nums):
            for item in d:
                if d[item]==target-a:
                    if item<i:return [item,i]
                    else: return [i,item]
            d[i]=a
        
    