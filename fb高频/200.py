class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(i, j):
            q, nq = [(i, j)], []
            while q:
                for x, y in q:
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if m > nx >= 0 <= ny < n and grid[nx][ny] == '1':
                            nq.append((nx, ny))
                            grid[nx][ny] = '0'
                q, nq = nq, []
                
        def dfs(i, j):
            for di, dj in directions:
                nx, ny = i + di, j + dj
                if m > nx >= 0 <= ny < n and grid[nx][ny] == '1':
                    grid[nx][ny] = '0'
                    dfs(nx, ny)
                
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i, j) # or dfs
                    res += 1
                
        return res
    
                
        
