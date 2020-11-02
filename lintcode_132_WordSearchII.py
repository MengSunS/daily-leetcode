class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here
        if not board or not words:
            return []
        res= set()
        
        for word in words:
            w= word[0]
     
            for i in range(len(board)):
                for j in range(len(board[0])):
                    visited= set()
                    if board[i][j]== w:      
                        visited.add((i, j))       
                        if self.dfs(board, word[1:], i, j, visited):
                            res.add(word)
                            break
                           
        return list(res)
    
    def dfs(self, board, word, i, j, visited):
        
        if word== '':
            return True
        
        for dx, dy in [(1,0), (0,1), (0,-1), (-1,0)]:
            nxt_x, nxt_y= i+dx, j+dy
            if self.isValid(nxt_x, nxt_y, visited, board) and board[nxt_x][nxt_y]==word[0]:
                visited.add((nxt_x, nxt_y))
                if self.dfs(board, word[1:], nxt_x, nxt_y, visited):
                    return True
                visited.remove((nxt_x, nxt_y))
        
        return False
    
    def isValid(self, x, y, visited, board):
        return 0<=x<len(board) and 0<=y<len(board[0]) and (x,y) not in visited
