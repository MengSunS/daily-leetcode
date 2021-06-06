# Method 1: translate into sliding window 

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        size = len(collections.Counter(s))
        res = 0
        for u in range(size + 1):
            res = max(res, self.helper(s, k, u))
        return res
    
    def helper(self, s, k, u):
        ans = i = 0
        m = {}
        n = len(s)
        for j in range(n):
            m[s[j]] = m.get(s[j], 0) + 1
            while len(m) > u:
                m[s[i]] -= 1
                if m[s[i]] == 0:
                    del m[s[i]] 
                i += 1
            if all(v >= k for v in m.values()):
                ans = max(ans, j - i + 1)
        return ans


# Method 2: Divide adn conquer

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        size = len(collections.Counter(s))
        res = 0
        for u in range(size + 1):
            res = max(res, self.helper(s, k, u))
        return res
    
    def helper(self, s, k, u):
        ans = i = 0
        m = {}
        n = len(s)
        for j in range(n):
            m[s[j]] = m.get(s[j], 0) + 1
            while len(m) > u:
                m[s[i]] -= 1
                if m[s[i]] == 0:
                    del m[s[i]] 
                i += 1
            if all(v >= k for v in m.values()):
                ans = max(ans, j - i + 1)
        return ans
