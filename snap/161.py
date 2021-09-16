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
                
        
