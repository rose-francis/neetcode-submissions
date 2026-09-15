class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre={i:[] for i in range(numCourses)}
        for crs,pr in prerequisites:
            pre[crs].append(pr)

        visiting=set()

        def dfs(crs):
            if crs in visiting:
                return False
            if pre[crs]==[]:
                return True

            visiting.add(crs)
            for pr in pre[crs]:
                if not dfs(pr):
                    return False
            visiting.remove(crs)
            pre[crs]=[]
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
            
        return True