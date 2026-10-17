class Solution:
    def trap(self, height: List[int]) -> int:
        prefix=[0]*len(height)
        suffix=[0]*len(height)
        maxp=maxs=0
        res=0
        for i in range(1,len(height)):
            maxp=max(maxp,height[i-1])
            prefix[i]=maxp

        for i in range(len(height)-2,-1,-1):
            maxs=max(maxs,height[i+1])
            suffix[i]=maxs
        
        for i in range(len(height)):
            water=(min(prefix[i],suffix[i])-height[i])
            if water>0:
                res+=water
        
        return res

