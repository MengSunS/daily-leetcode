class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m, n= len(maze), len(maze[0])
        hp= [(0, '', ball[0], ball[1])]
        directions= [(0, 1, 'r'),(1, 0, 'd'),(0, -1, 'l'),(-1, 0, 'u')]
        seen= {tuple(ball): (0, '')} 
        
        while hp:
            dist, path, x, y= heapq.heappop(hp)
            if [x, y]== hole:
                return path
            
            for dx, dy, d in directions:
                step= dist
                nx, ny= x, y
                
                while 0<= nx+ dx< m and 0<= ny+ dy< n and maze[nx+dx][ny+dy]!=1:
                    nx+= dx
                    ny+= dy
                    step+= 1
                    if [nx, ny]== hole:
                        break

                if (nx, ny) not in seen or seen[(nx, ny)]> (step, path+d):
                    seen[(nx, ny)]= (step, path+ d)
                    heapq.heappush(hp, (step, path+ d, nx, ny))
        return "impossible"
                    
                
                
        
