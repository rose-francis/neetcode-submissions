class Solution:
    def climbStairs(self, n: int) -> int:
        one, two=1,1
        for _ in range(n-1):
            s=one+two
            two=one
            one=s
        
        return one