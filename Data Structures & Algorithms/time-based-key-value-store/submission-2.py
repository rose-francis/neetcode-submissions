class TimeMap:

    def __init__(self):
        self.m=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res=""
        values= self.m.get(key,[])
        l=0
        r=len(values)-1
        while l<=r:
            m=(l+r)//2
            if values[m][1] == timestamp:
                return values[m][0]

            if values[m][1] > timestamp:
                r=m-1
            
            else:
                res=values[m][0]
                l=m+1
        
        return res
