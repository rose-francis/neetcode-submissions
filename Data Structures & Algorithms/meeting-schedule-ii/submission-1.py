"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n=len(intervals)
        if n<2:
            return n
        
        start=[]
        end=[]
        for i in range(n):
            start.append(intervals[i].start)
            end.append(intervals[i].end)
        
        start.sort()
        end.sort()

        s=0
        e=0
        count=0
        rooms=0
        while s<n:
            if start[s]< end[e]:
                s+=1
                count+=1
                rooms=max(rooms,count)
            else:
                e+=1
                count-=1    

        return rooms
