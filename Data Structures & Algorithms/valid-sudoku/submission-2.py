class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s=set()
            for j in range(9):
                if board[i][j]!="." and board[i][j] not in s:
                    s.add(board[i][j])
                elif board[i][j] in s:
                    return False
        
        for i in range(9):
            s=set()
            for j in range(9):
                if board[j][i]!="." and board[j][i] not in s:
                    s.add(board[j][i])
                elif board[j][i] in s:
                    return False
        
        for k in range(3):
            for m in range(3):
                s=set()
                for i in range(k*3,k*3+3):
                    for j in range(m*3,m*3+3):
                        if board[i][j]!="." and board[i][j] not in s:
                            s.add(board[i][j])
                        elif board[i][j] in s:
                            return False
        
        return True
                    

        