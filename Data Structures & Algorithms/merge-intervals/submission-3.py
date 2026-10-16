class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        res=[]
        if intervals[0][1]>=intervals[1][0]:
            new=[intervals[0][0], max(intervals[1][1],intervals[0][1])]
            res.append(new)
        else:
            res.append(intervals[0].copy())
            res.append(intervals[1].copy())
        for i in range(2,len(intervals)):
                e=len(res)-1
                if res[e][1]>=intervals[i][0]:
                    new=[res[e][0],max(intervals[i][1],res[e][1])]
                    res[e]=new
                else:
                    res.append(intervals[i])
            

        return res
