class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        max_vol=0
        while left<right:
            vol=min(heights[left],heights[right])*(right-left)
            if vol>max_vol:
                max_vol=vol
            if heights[left]<heights[right]:
                left+=1
            elif heights[left]>heights[right]:
                right-=1
            else:
                left+=1
                right-=1
        return max_vol
        



        