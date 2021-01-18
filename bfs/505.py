class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        q= [(0, start[0], start[1])]
        visited= {tuple(start): 0}
        m, n= len(maze), len(maze[0])
        directions= [(0,1),(1,0),(0,-1),(-1,0)]
         
        while q:
            # might be more layers, but less steps。不是数层数
            dist, x, y= heapq.heappop(q)
            if [x,y]==destination: 
                return dist
            for dx, dy in directions:
                nx, ny, step= x, y, 0
                while 0<= nx< m and 0<= ny< n and maze[nx][ny]!= 1:
                    nx+= dx
                    ny+= dy
                    step+= 1
                nx, ny, step= nx-dx, ny-dy, step-1
                if (nx, ny) not in visited or visited[(nx, ny)]> step+ dist:
                    visited[(nx, ny)]= step+ dist
                    heapq.heappush(q, (step+ dist, nx, ny))
                    
        return -1
       
        
