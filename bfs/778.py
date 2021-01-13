class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n= len(grid), len(grid[0])
        dir= {(0, 1),(0, -1),(1, 0),(-1, 0)}
        hp= [(grid[0][0], 0, 0)]
        seen= set()
        seen.add((0, 0))
        t= 0
        while hp:
            cur, x, y= heapq.heappop(hp)
            t= max(t, cur)
            if x==m-1 and y==n-1:
                return t
            for dx, dy in dir:
                nxt_x, nxt_y= x+ dx, y+ dy
                if nxt_x>= m or nxt_x<0 or nxt_y>=n or nxt_y<0:
                    continue
                if (nxt_x, nxt_y) in seen:
                    continue
                heapq.heappush(hp, (grid[nxt_x][nxt_y], nxt_x, nxt_y))
                seen.add((nxt_x, nxt_y))
        return -1
            
##imagine一个点开始，neighbors水平线低的都在最前面，继续往复浸染 不管高的矮的neighbors，直到遇到更高的水平线瞬间拔高，以此继续        
