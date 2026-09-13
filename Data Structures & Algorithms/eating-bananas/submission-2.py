class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        total=sum(piles)
        right=total
        min_k=0
        while left<=right:
            k=(left+right)//2
            if k*h>=total:
                hr=h
                for j in piles:
                    if j<k:
                        hr-=1
                    else:
                        hr-=math.ceil(j/k)
                    if hr<0:
                        left=k+1
                if hr>=0:
                    right=k-1
                    min_k=k
            else:
                left=k+1

        return min_k


