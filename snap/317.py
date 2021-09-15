class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        buildings = sum([grid[i][j] == 1 for i in range(m) for j in range(n)])
        distSum = [[0] * n for _ in range(m)]
        hits = [[0] * n for _ in range(m)]
        def bfs(x, y, buildings):
            q, nq = [(x, y, 0)], []
            seen = set([(x, y)])
            count = 0
            while q:
                for x, y, steps in q:
                    for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                        if m > nx >= 0 <= ny < n and (nx, ny) not in seen and grid[nx][ny] != 2:
                            seen.add((nx, ny)) #致命错误：忘了加入seen set
                            if grid[nx][ny] == 0:
                                distSum[nx][ny] += steps + 1
                                hits[nx][ny] += 1
                                nq.append((nx, ny, steps + 1)) #致命错误：忘了append
                            else:
                                count += 1        
                q, nq = nq, []
            return count == buildings
            
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    if bfs(x, y, buildings) == -1:
                        return -1
       
        return min([distSum[x][y] for x in range(m) for y in range(n) if grid[x][y] == 0 and hits[x][y] == buildings] or [-1])
       
                        
            
        
