class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        
        def dfs(i, j):
            count = 1
            grid[i][j] = 2
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if m > ni >= 0 <= nj < n and grid[ni][nj] == 1:  
                    count += dfs(ni, nj)
            
            return count
        
        def isConnected(i, j):
            if i == 0: 
                return True
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if m > ni >= 0 <= nj < n and grid[ni][nj] == 2:
                    return True
            return False
        
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for i, j in hits:
            grid[i][j] *= -1
       
                
        for j in range(n):
            if grid[0][j] == 1:
                dfs(0, j)
       
     
      
        res = []
        hits = hits[::-1]
        for i, j in hits:
            if grid[i][j] != -1:
                res.append(0)
                continue
            else:
                if isConnected(i, j):
                    
                    res.append(dfs(i, j) - 1)
                else:
                    grid[i][j] = 1
                    res.append(0)
                    
            
        return res[::-1]
               

                
            

        
        

        
        
        
                    
                    
