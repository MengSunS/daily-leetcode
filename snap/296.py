class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        all_r = [i for i in range(m) for j in range(n) if grid[i][j]]
        all_c = [j for j in range(n) for i in range(m) if grid[i][j]]
        
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j]:
        #             all_r.append(i)
        #             all_c.append(j)
        # all_c.sort()
        x, y = all_r[len(all_r) // 2], all_c[len(all_c) // 2] # median
        return sum([abs(x - i) for i in all_r])+ sum([abs(y - j) for j in all_c])
                    
        
