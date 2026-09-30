class MedianFinder:

    def __init__(self):
        self.small=[]
        self.large=[]
        
    def addNum(self, num: int) -> None:
        if self.small==[] or num<-1*self.small[0]:
            heapq.heappush(self.small,-1*num)
        else:
            heapq.heappush(self.large, num)
        
        if len(self.small)-len(self.large)>1:
            val=-1*heapq.heappop(self.small)
            heapq.heappush(self.large,val)

        elif len(self.large)-len(self.small)>1:
            val=heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)

    def findMedian(self) -> float:
        s=len(self.small)
        l=len(self.large)
        if s==l:
            return ((-1*self.small[0]+self.large[0])/2)
        elif s>l:
            return -1*self.small[0]
        else:
            return self.large[0]
        
        