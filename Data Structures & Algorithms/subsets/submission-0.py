class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums==[]:
            return []
        if len(nums)==1:
            return [[],[nums[0]]]
        
        res=[[],[nums[0]]]
        for i in range(1,len(nums)):
            l=len(res)
            for j in range(l):
                x=res[j]+[nums[i]]
                res.append(x)

        return res
                

