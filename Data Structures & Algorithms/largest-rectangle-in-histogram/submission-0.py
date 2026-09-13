class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l=len(heights)
        max_area=0
        for i in range(l):
            left=0
            right=l-1
            j=i-1
            while j>=0:
                if heights[j]<heights[i]:
                    left=j+1
                    break
                j-=1
            for k in range(i+1,l):
                if heights[k]<heights[i]:
                    right=k-1
                    break
            area=(right-left+1)*heights[i]
            if area>max_area:
                max_area=area
        
        return max_area
                





        
        return max_area

