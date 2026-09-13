class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        prefix=[0]*n
        suffix=[0]*n
        area=0
        for i in range(1,n):
            l_max=max(prefix[i-1],height[i-1])
            prefix[i]=l_max
        
        for i in range(n-2,-1,-1):
            r_max=max(height[i+1],suffix[i+1])
            suffix[i]=r_max

        for i in range(n):
            m=min(prefix[i],suffix[i])-height[i]
            if m>=0:
                area+=m
        
        return area
            
        