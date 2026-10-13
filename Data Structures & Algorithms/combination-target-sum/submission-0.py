class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        n=len(nums)
        new=[]
        self.c_sum=0
        def dfs(i):
            if self.c_sum==target:
                res.append(new.copy())
                return
            for j in range(i,n):
                if self.c_sum+nums[j] <=target:
                    self.c_sum+=nums[j]
                    new.append(nums[j])
                    dfs(j)
                    self.c_sum-=nums[j]
                    new.pop()

        
        dfs(0)
        return res