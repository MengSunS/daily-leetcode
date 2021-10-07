class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if s == t: return False
        i, j = 0, 0
        while i < m and j < n and s[i] == t[j]:
            i += 1
            j += 1
        if m > n: return s[i + 1:] == t[j:]
        elif m < n: return s[i:] == t[j+1:]
        else: return s[i+1:] == t[j+1:]
      

  # O(N)
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)
        if s == t or len(t) - len(s) > 1:
            return False
        for i in range(len(s)):
            if s[i] != t[i]:
                return s[i + 1:] == t[i + 1:] or s[i:] == t[i + 1:]
        return True
                
        
