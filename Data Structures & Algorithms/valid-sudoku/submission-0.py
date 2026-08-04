class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #rows
        for row in board:
            seen = set()
            for cell in row:
                if cell in seen:
                    return False
                if cell != '.':    
                    seen.add(cell)    
            
        #columns
        for i in range(0, 9):
            seen = set()
            for j in range(0, 9):
                if board[j][i] in seen:
                    return False
                if board[j][i] != '.':    
                    seen.add(board[j][i]) 

        #boxes
        for rowB in range(0, 6, 3):
            for colB in range(0, 6, 3):
                seen = set()
                for i in range(rowB, rowB+3):
                    for j in range(colB, colB+3):
                        if board[i][j] in seen:
                            return False
                        if board[i][j] != '.':    
                            seen.add(board[i][j])    

        return True
         
# validate each row // done
# validate each column // done
# validate boxes

# i = 0 j=0; j+=3
#k = i - , p = j- j+3