class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda e: e[0])

        res=[intervals[0]]
        for i in range(1,len(intervals)):
            if res[-1][1]>=intervals[i][0]:
                new=[res[-1][0], max(res[-1][1],intervals[i][1])]
                res.pop()
                res.append(new)
            else:
                res.append(intervals[i])
        
        return res
