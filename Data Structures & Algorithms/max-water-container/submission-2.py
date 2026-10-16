class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res=0
        l=0
        r=len(heights)-1
        while l<r:
            area=min(heights[l],heights[r])*(r-l)
            res=max(area,res)
            if heights[l]>heights[r]:
                r-=1
            elif heights[r]>heights[l]:
                l+=1
            else:
                if heights[l+1]>heights[r-1]:
                    l+=1
                else:
                    r-=1
                
        return res
