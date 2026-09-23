class Solution:
    def rob(self, nums: List[int]) -> int:
        cache={}
        def dfs( i):
            if i>=len(nums):
                return 0
            if i+1 in cache:
                one=cache[i+1]
            else:
                one=dfs(i+1)
                cache[i+1]=one
            if i+2 in cache:
                two= cache[i+2]
            else:
                two=dfs(i+2)
                cache[i+2]=two
            return max(nums[i]+two,one)
        
        return dfs(0)