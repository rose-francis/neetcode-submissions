class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            elements=set()
            for j in i:
                if j!=".":
                    if j in elements:
                        return False
                    else:
                        elements.add(j)
        
        for i in range(9):
            elements=set()
            for j in board:
                if j[i]!=".":
                    if j[i] in elements:
                        return False
                    else:
                        elements.add(j[i])
       
        for i in range(0,6,3):
            for j in range(0,6,3):
                elements=set()
                for a in range(i,i+3):
                    for b in range(j,j+3):
                        if board[a][b]!=".":
                            if board[a][b] in elements:
                                return False
                            else:
                                elements.add(board[a][b])
            
           
        
        return True



        