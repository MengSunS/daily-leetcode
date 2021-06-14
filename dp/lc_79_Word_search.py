class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word or not board: return False
        m, n= len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                visited= set() #不能放在循环外
                if board[i][j]== word[0]:
                    visited.add((i, j))
                    if self.dfs(board, word[1:], i, j, visited):
                        return True

        return False
 
    
    def dfs(self, board, word, i, j, visited):
        if not word:
            return True
        
       
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nxt_x, nxt_y= i+ dx, j+ dy
            if 0<= nxt_x< len(board) and 0<= nxt_y< len(board[0]) and (nxt_x, nxt_y) not in visited and board[nxt_x][nxt_y]== word[0]:
                visited.add((nxt_x, nxt_y))
                if self.dfs(board, word[1:], nxt_x, nxt_y, visited): #这里不能写成ans= self.dfs(),最后return ans的形式，因为找一个就return true并结束了，不需要也不能走下一个candidates并覆盖
                    return True
                visited.remove((nxt_x, nxt_y))
                
        
                
      
   
  
            
    
        
    
