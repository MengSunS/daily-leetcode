class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, missing = Counter(t), len(t)
        i, j = 0, 0
        res_i, res_j = 0, float('inf')
        for j in range(len(s)):
            if s[j] in need:
                need[s[j]] -= 1
                if need[s[j]] >= 0:
                    missing -= 1
            while missing == 0:
                if j - i + 1 < res_j - res_i + 1:
                    res_i, res_j = i, j
                if s[i] in need:
                    need[s[i]] += 1
                    if need[s[i]] > 0:
                        missing += 1
                i += 1
        return s[res_i: res_j + 1] if res_j != float('inf') else ""
                        
        
