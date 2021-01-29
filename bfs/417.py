class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or len(matrix)== 0: return 
        m, n= len(matrix), len(matrix[0])
        pc, ac= [[0]*n for _ in range(m)], [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i== 0 or j== 0:
                    pc[i][j]= 1
                if i== m-1 or j== n-1:
                    ac[i][j]= 1
                    
        for i in range(m):
            self.bfs(matrix, pc, i, 0, m, n)
            self.bfs(matrix, ac, i, n-1, m, n)
        for j in range(n):
            self.bfs(matrix, pc, 0, j, m, n)
            self.bfs(matrix, ac, m-1, j, m, n)
        res= []
        for i in range(m):
            for j in range(n):
                if pc[i][j]== ac[i][j]== 1:
                    res.append([i, j])
        return res

    def bfs(self, matrix, record, x, y, m, n):
        q= deque([(x, y)])
        while q:
            x, y= q.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny= x+ dx, y+ dy
                if nx>= m or nx< 0 or ny>= n or ny< 0:
                    continue
                if record[nx][ny]==1:
                    continue
                if matrix[nx][ny]>= matrix[x][y]:
                    record[nx][ny]=1
                    q.append((nx, ny))
    # 思路: 若从每个点出发顺流而下检查是否能到达太平洋也能到达大西洋，那么找到一个洋也不能停因为还要找另外一个洋，最坏把所有路径全找一遍指数级，再乘以mn。如果一个点能到一个洋，那么这条路径上的所有点都能到，但我们不知道这条路径能不能到，难道都要记下来？；若从边界出发，那就是从答案出发逆流而上而到的反过来就是顺流而下能到答案的，这个地方去重的是一个点若已经标记能到，代表这个点能顺流而下找到之前loop里的答案出口，在当前层代表也能到达当前答案出口，在之前第一次找到这个点时就已经把这个点上下左右都放进去了。这个去重机制就是最基本的bfs类似多个starting nodes，层内nodes之间的后续去重+一个node后续，就只是很直白的把starting nodes连接的图扫了一遍 
                
                
        
        
        
