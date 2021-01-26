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
        
                    
            
                
        
