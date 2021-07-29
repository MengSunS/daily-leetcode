class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(pos):
            if pos == n:
                self.res = max(self.res, len(path))
                return 
            for i in range(pos, n):
                cur = s[pos: i + 1]
                if cur not in path and len(path) + 1 + n - i > self.res: #强剪枝
                    path.add(cur)
                    dfs(i + 1)
                    path.remove(cur)
        path = set()
        self.res = 0
        n = len(s)
        dfs(0)
        return self.res
        
