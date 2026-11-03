class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l=1
        r=max(piles)
        mink=r
        while l<=r:
            m=(l+r)//2
            s=0
            for p in piles:
                s+=math.ceil(p/m)
            if s>h:
                l=m+1
            else:
                mink=min(mink,m)
                r=m-1
        return mink
