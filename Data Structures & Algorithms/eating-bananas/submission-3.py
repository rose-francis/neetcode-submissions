class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        total=sum(piles)
        r=max(piles)
        min_k=0
        while l<=r:
            k=(l+r)//2
            hr=h
            for j in piles:
                hr-=math.ceil(j/k)
                if hr<0:
                    l=k+1
                    break
            if hr>=0:
                r=k-1
                min_k=k
            

        return min_k


