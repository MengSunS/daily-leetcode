# 题意： (i + 1) count and say ith result
class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for i in range(n - 1):
            res = self.next(res)
        return res
    
    def next(self, s):
        i = 0
        n = len(s)
        res = ''
        while i < n:
            cnt = 1
            while i + 1 < n and s[i + 1] == s[i]:
                i += 1
                cnt += 1
            res += str(cnt) + s[i]
            i += 1
        return res
        
    
            
        
