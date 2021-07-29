
class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
        anti = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}
        valid = {}
        valid[(0, 0)] = master.isTarget()
        
        def dfs(x, y):
            for d in dirs: 
                nx, ny = x + dirs[d][0], y + dirs[d][1]
                if (nx, ny) not in valid and master.canMove(d):
                    master.move(d)
                    valid[(nx, ny)] = master.isTarget()
                    dfs(nx, ny)
                    master.move(anti[d])
                    
        dfs(0, 0)
        q = collections.deque([(0, 0, 0)])
        seen = set([(0, 0)])
        while q:
            x, y, steps = q.popleft()
            if valid[(x, y)]: 
                return steps
            for d in dirs:
                nx, ny = x + dirs[d][0], y + dirs[d][1]
                if (nx, ny) in valid and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    q.append((nx, ny, steps + 1))
        return -1 
                   
        

