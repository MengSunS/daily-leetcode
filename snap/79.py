class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, pos):
            if pos == len(word): return True
            if not m > i >= 0 <= j < n: return False
            if word[pos] != board[i][j]: return False
            
            tmp = board[i][j]
            board[i][j] = '#'
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if dfs(ni, nj, pos + 1):
                    return True
            board[i][j] = tmp
            return False
            
  
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True                  
        return False
        
