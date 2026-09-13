class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right=max(piles)
        left=1
        while left<=right:
            mid=(left+right)//2
            sum=0
            for i in piles:
                sum+=math.ceil(i/mid)
            if sum<=h:
                k=mid
                right=mid-1
            else:
                left=mid+1
        return k
            



        