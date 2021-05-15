# O(N)
class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        l = {c: i for i, c in reversed(list(enumerate(s)))} #O(N)
        r = {c: i for i, c in enumerate(s)}
        intervals = []
        for c in set(s): # O(26*N)
            b, e = l[c], r[c]
            i = b
            while i < e and b == l[c]:
                b, e = min(b, l[s[i]]), max(e, r[s[i]])
                i += 1
            if b == l[c]:
                intervals.append([e, b])
        res = []
        intervals.sort()  #O(26log26)
        prev = -1
        for e, b in intervals:
            if b > prev:
                res.append(s[b:e + 1])
            prev = e
        return res
                
        
        
                
        
