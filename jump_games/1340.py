class Solution:
    def maxJumps(self, A: List[int], d: int) -> int:
        n = len(A)
        @lru_cache(None)
        def dp(i):
            ans = 1
            for di in [-1, 1]:
                for index in range(i + di, i + di * d + di, di):
                    if index >= n or index < 0 or A[index] >= A[i]:
                        break
                    ans = max(ans, 1 + dp(index))
            return ans
        
        return max(map(dp, range(n)))
                    
 

# 329. Longest Increasing Path in a Matrix

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        @lru_cache(None)
        def dp(i,j):
            ans = 1
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if ni >= m or ni < 0 or nj >= n or nj < 0 or matrix[ni][nj] <= matrix[i][j]:
                    continue
                ans = max(ans, dp(ni, nj) + 1)
            return ans
        
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dp(i, j))
        return res
                
         
