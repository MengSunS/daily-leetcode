class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        q= deque([start])
        directions= [(0,1),(1,0),(0,-1),(-1,0)]
        m, n= len(maze), len(maze[0])
        visited= set(start)
        while q:
            x, y= q.popleft()
            if [x,y]==destination: 
                return True
            for dx, dy in directions:
                nx, ny= x+ dx, y+ dy
                #放进q的是要继续传播的，单向路上的点不需要放进q，也无需check visited?
                while 0<= nx< m and 0<= ny< n and maze[nx][ny]!= 1:
                    nx, ny= nx+dx, ny+dy
                lastx, lasty= nx-dx, ny-dy
                if 0<=lastx<m and 0<=lasty<n and (lastx, lasty) not in visited:
                    visited.add((lastx,lasty))
                    q.append([lastx, lasty])
        return False
       
       
       
        
        
