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
    
                
# Union Find

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        parent = [i for i in range(m * n)]
        self.cnt = sum(grid[i][j] == '1' for i in range(m) for j in range(n))
       
        # def find(x):
        #     y = x
        #     while y != parent[y]:
        #         y = parent[y]
        #     while x != y:
        #         px = parent[x]
        #         parent[x] = y
        #         x = px
        #     return y
        
        def find(x):
            if x != parent[x]:
                return find(parent[x])
            return x
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                self.cnt -= 1
                parent[root_x] = root_y
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                index = i * n + j
                if j < n - 1 and grid[i][j + 1] == '1':
                    union(index, index + 1)
                if i < m - 1 and grid[i + 1][j] == '1':
                    union(index, index + n)
        
        return self.cnt
                    
            
          
