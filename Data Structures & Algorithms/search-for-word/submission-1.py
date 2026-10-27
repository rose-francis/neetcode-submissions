class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        s=set()

        def dfs(li, i):
            row,col=li
            if row>=m or row<0 or col>=n or col<0 or board[row][col]!=word[i] or (row,col) in s:
                return False

            if i==len(word)-1:
                return True

            if (row,col) not in s:
                s.add((row,col))
            
                if dfs([row+1,col],i+1):
                    return True
                if dfs([row,col+1],i+1):
                    return True
                if dfs([row-1,col],i+1):
                    return True
                if dfs([row,col-1],i+1):
                    return True
                s.remove((row,col))

        for i in range(m):
            for j in range(n):
                if dfs([i,j],0):
                    return True

        return False

            