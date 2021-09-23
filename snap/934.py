# 第一步dfs or bfs都可以，dfs写起来更简单，第二步bfs. 
# traverse的dfs visisted, res.append()都写在最开头外面，边走边记。
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        bfs = []
        def dfs(i, j):
            grid[i][j] = -1
            bfs.append((i, j))
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if m > ni >= 0 <= nj < n and grid[ni][nj] == 1:
                    dfs(ni, nj)
       
        def first():        
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        return i, j
        
        dfs(*first())
        step = 0
        new = []
        
        while bfs:
            for i, j in bfs:
                for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if m > ni >= 0 <= nj < n:
                        if grid[ni][nj] == 1:
                            return step
                        elif grid[ni][nj] == 0:
                            grid[ni][nj] = -1 
                            new.append((ni, nj))
                            
            bfs, new = new, []
            step += 1

                    
                
            
        
