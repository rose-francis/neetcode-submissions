class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack=[]
        maxA=0
        for i,h in enumerate(heights):
            s=i
            while stack and stack[-1][1]>= h:
                s,he=stack.pop()
                maxA=max(maxA, (i-s)*he)
            stack.append([s,h])

        for i,h in stack:
            maxA= max(maxA, h*(len(heights)-i))

        return maxA