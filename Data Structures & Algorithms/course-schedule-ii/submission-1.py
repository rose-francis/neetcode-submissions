class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
      indegree=[0]* numCourses
      adj=[[] for i in range(numCourses)]
      for crs,pre in prerequisites:
        indegree[pre]+=1
        adj[crs].append(pre)
      
      q=deque()
      for i in range(numCourses):
        if indegree[i]==0:
          q.append(i)
      
      output=[]
      while q:
        crs=q.popleft()
        output.append(crs)
        for i in adj[crs]:
          indegree[i]-=1
          if indegree[i]==0:
            q.append(i)
        
      
      if len(output)==numCourses:
        return output[::-1]
      return []

        