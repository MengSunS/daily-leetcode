class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        
       
        m, n= len(grid), len(grid[0])
        q= deque()
        count= 0
        directions= [(0, 1),(1, 0),(0, -1),(-1, 0)]
        seen= collections.defaultdict(set)

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='@':
                    q.append((i, j, 0, 0))
                if 'a'<=grid[i][j]<='f':
                    count+= 1
        final_state= 0
        for i in range(count):
            final_state |= (1<<i)
        
        while q:
            x, y, state, step= q.popleft()
            if state== final_state:
                return step
            for dx, dy in directions:
                nx, ny= x+ dx, y+ dy
                new_state= state
                if nx>=m or nx<0 or ny>=n or ny<0:
                    continue
                if grid[nx][ny]=='#':
                    continue
                if 'A'<= grid[nx][ny]<= 'F':
                    k= ord(grid[nx][ny])- ord('A')
                    if state & (1 << k) == 0:
                        continue
                if 'a'<= grid[nx][ny]<= 'f':
                    k= ord(grid[nx][ny])- ord('a')
                    new_state |= (1 << k)
                if new_state in seen[(nx, ny)]:
                    continue

                q.append((nx, ny, new_state, step+ 1))
                seen[(nx, ny)].add(new_state)
        return -1
                    
                        
                        
            
            
                
        
                    
                
        
