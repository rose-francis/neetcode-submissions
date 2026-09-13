class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res=0
        m=len(grid)
        n=len(grid[0])
        
        def dfs(i,j):
            
            if grid[i][j]=="0":
                return
            
            
            grid[i][j]="0"

            if j+1<n:
                dfs(i,j+1)
            if j-1>=0:
                dfs(i,j-1)
            if i+1<m:
                dfs(i+1,j)
            if i-1>=0:
                dfs(i-1,j)
            
                
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    res+=1
                    dfs(i,j)
        return res
                
