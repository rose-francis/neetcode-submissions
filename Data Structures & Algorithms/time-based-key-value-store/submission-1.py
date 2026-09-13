class TimeMap:

    def __init__(self):
        self.time_map=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        max_time=-1
        val=None
        l=0
        r=len(self.time_map[key])-1
        while l<=r:
            m=(l+r)//2
            if self.time_map[key][m][1] == timestamp:
                return self.time_map[key][m][0]

            if self.time_map[key][m][1] > timestamp:
                r=m-1
            
            else:
                max_time=self.time_map[key][m][1]
                val=self.time_map[key][m][0]
                l=m+1
        
        if not val:
            return ""
        return val

