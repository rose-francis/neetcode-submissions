class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        
        target=sum(nums)//2
        n=len(nums)
        s=set()

        for i in range(n-1,-1,-1):
            if s==set():
                s.add(nums[i])
                s.add(0)
            else:
                new=set()
                for a in s:
                    new.add(nums[i]+a)
                s=s.union(new)
        
        if target in s:
            return True
        else:
            return False
        
      

