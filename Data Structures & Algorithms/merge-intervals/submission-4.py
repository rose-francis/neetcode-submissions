class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        res=[intervals[0]]
        for i in range(1,len(intervals)):
                e=len(res)-1
                if res[e][1]>=intervals[i][0]:
                    new=[res[e][0],max(intervals[i][1],res[e][1])]
                    res[e]=new
                else:
                    res.append(intervals[i])
            

        return res
