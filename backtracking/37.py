class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.dfs(board)
            
        
    
    def dfs(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]!= '.': continue
                for k in range(1, 10):
                    if not self.isValid(board, i, j, str(k)):
                        continue
                    board[i][j]= str(k)
                    if self.dfs(board):
                        return True
                    board[i][j]= '.'
                return False
        return True
                    
        
            
    def isValid(self, board, x, y, k):
        for i in range(9):
            if board[i][y]== k: return False
            if board[x][i]== k: return False
            if board[x//3*3+ i//3][y//3*3+ i%3]== k: return False
        return True
        
            
        
