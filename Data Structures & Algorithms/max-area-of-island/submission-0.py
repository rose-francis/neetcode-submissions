class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res=0
        m=len(grid)
        n=len(grid[0])
        
        def dfs(i,j):
            if ( i<0 or i>=m or j<0 or j>=n or grid[i][j]==0 ):
                return
            
            grid[i][j]=0
            self.area+=1
            dfs(i,j-1)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i+1,j)

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    self.area=0
                    dfs(i,j)
                    res=max(res,self.area)

        return res