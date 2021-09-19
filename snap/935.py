O(n) time, maybe O(100) time.见leet神的具体写法

class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dct = {1:[6, 8], 2:[7, 9], 3:[4, 8], 4:[0, 3, 9], 5:[], 6:[0, 1, 7], 7:[2, 6], 8:[1, 3], 9:[2, 4], 0:[4, 6]}
        dp = [1] * 10
        for _ in range(n - 1):
            nxt = [0] * 10
            for i in range(10):
                for j in dct[i]:
                    nxt[j] += dp[i]
            dp = nxt
        return sum(dp) % MOD



# dfs with memo top down

class Solution:
    def knightDialer(self, k: int) -> int:
        def dfs(x, y, left, memo):
            if (x, y, left) in memo:
                return memo[(x, y, left)]
            if left == 0:
                return 1
            memo[(x, y, left)] = 0
            for nx, ny in [(x + 2, y + 1), (x + 2, y - 1), (x - 2, y + 1), (x - 2, y - 1), (x + 1, y + 2), (x + 1, y - 2), (x - 1, y + 2), (x - 1, y - 2)]:
                if m > nx >= 0 <= ny < n and (nx, ny) not in {(m - 1, 0), (m - 1, n - 1)}:
                    memo[(x, y, left)] += dfs(nx, ny, left - 1, memo)
            return memo[(x, y, left)]
        
        self.MOD = 10 ** 9 + 7
        m, n = 4, 3
        res = 0
        memo = {}
        for i in range(m):
            for j in range(n):
                if (i, j) not in {(m - 1, 0), (m - 1, n - 1)}:
                    res += dfs(i, j, k - 1, memo)
        return res % self.MOD
            
