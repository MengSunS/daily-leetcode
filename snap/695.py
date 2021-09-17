class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(x, y):
            q, nq = [(x, y)], []
            grid[x][y] = 0
            cnt = 0
            while q:
                cnt += len(q)
                for x, y in q:
                    # grid[x][y] = 0 #错点，不可以只写在这，下一层child当node是共同的，放进去两次
                    for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                        if m > nx >= 0 <= ny < n and grid[nx][ny] == 1:
                            nq.append((nx, ny))
                            grid[nx][ny] = 0 #去重一定在里面去重！！！
                q, nq = nq, []
            return cnt
        
        def dfs(x, y):
            grid[i][j] = 0
            tmp = 1
            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if m > nx >= 0 <= ny < n and grid[nx][ny] == 1:
                    grid[nx][ny] = 0
                    tmp += dfs(nx, ny)
            return tmp
            
 
        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res 
                    
      
