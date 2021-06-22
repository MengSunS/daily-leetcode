# method 1: bfs

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        q = collections.deque([])
        for i in range(m):
            for j in range(n):
                if (i in [0, m - 1] or j in [0, n -1]) and board[i][j] == 'O':
                    q.append([i, j])
                    board[i][j] = '.'
        
        while q:
            r, c = q.popleft()
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if m > nr >= 0 <= nc < n and board[nr][nc] == 'O':
                    board[nr][nc] = '.'
                    q.append([nr, nc])
                  
        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


# method 2: dfs

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        if not board or not board[0]: return 
        for i in [0, m - 1]:
            for j in range(n):
                self.dfs(i, j, board)
        for i in range(m):
            for j in [0, n - 1]:
                self.dfs(i, j, board)
                
        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        
    def dfs(self, i, j, board):
        if len(board) > i >= 0 <= j < len(board[0]) and board[i][j] == 'O':
            board[i][j] = '.'
            self.dfs(i + 1, j, board)
            self.dfs(i, j + 1, board)
            self.dfs(i - 1, j, board)
            self.dfs(i, j - 1, board)
    
