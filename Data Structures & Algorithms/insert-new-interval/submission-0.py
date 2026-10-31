class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        flag=0
        for i in range(len(intervals)):
            if intervals[i][0]>=newInterval[0]:
                intervals.insert(i,newInterval)
                flag=1
                break
        
        if flag==0:
            intervals.append(newInterval)

        res=[]
        for i in range(len(intervals)):
            if not res:
                res.append(intervals[i])
            
            if res[-1][1]>=intervals[i][0]:
                new=[res[-1][0], max(res[-1][1],intervals[i][1])]
                res.pop()
                res.append(new)
            else:
                res.append(intervals[i])
            
        return res