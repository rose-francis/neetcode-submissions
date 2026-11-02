class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp=[-1]*len(nums)

        def dfs(i):
            if i==len(nums)-1:
                return True
            
            if i>=len(nums):
                return False
            
            if dp[i]!=-1:
                    return dp[i]   

            for j in range(1,nums[i]+1):
                if (i+j)<len(nums) and dfs(i+j):
                    dp[i]=True
                    return True

            dp[i]= False
            return False

        return dfs(0)