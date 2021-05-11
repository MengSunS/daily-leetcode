# lee215 

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * n for _ in range(m)]
        dire = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        k = 0
        bfs = []
        def dfs(r, c):
            if r >= m or r < 0 or c >= n or c < 0 or dp[r][c] != float('inf'):
                return 
            dp[r][c] = k
            bfs.append((r, c))
            dfs(r + dire[grid[r][c] - 1][0], c + dire[grid[r][c] - 1][1])
        
        dfs(0, 0)
        while bfs:
            k += 1
            bfs, bfs2 = [], bfs
            [dfs(x + dx, y + dy) for x, y in bfs2 for dx, dy in dire]
        return dp[-1][-1]
        
















class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        # bfs minimum layers, when layers are defined by number of changes
        m, n= len(grid), len(grid[0])
        q= deque()
        tmp= []
        visited= set()
        dir= [(0, 1),(0, -1),(1, 0),(-1, 0)]
        self.flow(grid, 0, 0, visited, q, m, n)
        
        step= 0
        while q:
            for _ in range(len(q)):
                x, y= q.popleft()
                if (x, y)== (m-1, n-1):
                    return step
                for dx, dy in dir:
                    nx, ny= x+ dx, y+ dy
                    if nx>= m or nx< 0 or ny>= n or ny< 0:
                        continue
                    if (nx, ny) in visited: 
                        continue
                    self.flow(grid, nx, ny, visited, q, m, n)
                    
            step+= 1
        
    def flow(self, grid, x, y, visited, q, m, n):
        
        if (x, y) in visited: return 
        if x>= m or x< 0 or y>= n or y< 0: return 
        
        visited.add((x, y))
        q.append((x, y))
        if grid[x][y]== 1:
            y+= 1
        elif grid[x][y]== 2:
            y-= 1
        elif grid[x][y]== 3:
            x+= 1
        else:
            x-= 1
        self.flow(grid, x, y, visited, q, m, n)
        
                    
            
                
        
