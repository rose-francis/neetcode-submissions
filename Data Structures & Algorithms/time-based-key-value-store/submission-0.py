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
        for entry in self.time_map[key]:
            if entry[1]<=timestamp and entry[1]>max_time:
                max_time=entry[1]
                val=entry[0]
        if val==None:
            return ""
        return val
