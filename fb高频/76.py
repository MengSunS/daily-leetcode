class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, missing = collections.Counter(t), len(t)
        start, end = -1, -1
        i = 0 
        for j in range(len(s)):
            if s[j] in need:
                need[s[j]] -= 1
                if need[s[j]] >= 0:
                    missing -= 1
            while missing == 0:
                if end == -1 or j - i + 1 < end - start + 1:
                    start, end = i, j
                if s[i] in need:
                    need[s[i]] += 1
                    if need[s[i]] > 0:
                        missing += 1
                i += 1
        return s[start: end + 1] if end != -1 else ''
            
