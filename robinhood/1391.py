class Solution:
    def hasValidPath(self, A: List[List[int]]) -> bool:
        m, n = len(A), len(A[0])
        parent = {(i, j): (i, j) for i in range(-1, 2 * m) for j in range(-1, 2 * n)}
        def find(x):
            i = x
            while i != parent[i]:
                i = parent[i]
            while i != x:
                tmp = parent[x]
                parent[x] = i
                x = tmp
            return i
        
        def union(i, j, di, dj):
            fx, fy = find((i, j)), find((i + di, j + dj))
            if fx != fy:
                parent[fx] = fy
                
        for i in range(m):
            for j in range(n):
                if A[i][j] in [2, 5, 6]: union(i * 2, j * 2, -1, 0)
                if A[i][j] in [1, 3, 5]: union(i * 2, j * 2, 0, -1)
                if A[i][j] in [2, 3, 4]: union(i * 2, j * 2, 1, 0)
                if A[i][j] in [1, 4, 6]: union(i * 2, j * 2, 0, 1)
        return find((0, 0)) == find((m * 2 - 2, n * 2 - 2))
    
    

        class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        dirs = {1: [(0, -1), (0, 1)], 
                2: [(-1, 0), (1, 0)],
                3: [(0, -1), (1, 0)],
                4: [(0, 1), (1, 0)],
                5: [(0, -1), (-1, 0)],
                6: [(0, 1), (-1, 0)]}
        def dfs(i, j, seen):
            if (i, j) == (m - 1, n - 1):
                return True
            for di, dj in dirs[grid[i][j]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen and (-di, -dj) in dirs[grid[ni][nj]]:
                    seen.add((ni, nj))
                    if dfs(ni, nj, seen):
                        return True
                    # seen.remove((ni, nj))
            return False
        
        return dfs(0, 0, set())
        
