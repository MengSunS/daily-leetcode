class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        res, n = 0, len(s)
        i, j = 0, 0
        while j < n:
            if s[j] in seen:
                i = max(i, seen[s[j]] + 1)
            res = max(res, j - i + 1)
            seen[s[j]] = j
            j += 1
        return res
                

def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        res, i, n = 0, 0, len(s)
        
        for j in range(n):
            if s[j] not in seen:
                seen.add(s[j])
                res = max(res, j - i + 1)
            else:
                while s[i] != s[j]:
                    seen.remove(s[i])
                    i += 1
                i += 1
        return res 
