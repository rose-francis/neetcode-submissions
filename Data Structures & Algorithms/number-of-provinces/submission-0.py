class DSU:
    def __init__(self,n):
        self.parent=list(range(n))
        self.rank=[1]*n
    
    def find(self,node):
        cur=node
        while cur!=self.parent[cur]:
            self.parent[cur]=self.parent[self.parent[cur]]
            cur=self.parent[cur]
        return cur

    def union(self,i,j):
        pi=self.find(i)
        pj=self.find(j)
        if pi==pj:
            return False
        if self.rank[pj]>self.rank[pi]:
            pi,pj=pj,pi
        self.parent[pj]=pi
        self.rank[pi]+=self.rank[pj]
        return True


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        res=n
        dsu=DSU(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1 and dsu.union(i,j):
                    res-=1
        return res