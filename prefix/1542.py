class Solution:
    def longestAwesome(self, s: str) -> int:
        n, cur, res = len(s), 0, 0
        seen = [-1] + [inf] * pow(2, 10)
        for i, a in enumerate(s):
            cur ^= (1 << int(a))
            for b in range(10):
                res = max(res, i - seen[cur ^ (1 << b)])
            res = max(res, i - seen[cur])
            seen[cur] = min(seen[cur], i)
        return res
            
            
            
        
