class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = i = 0
        m = {}
        for j in range(len(s)):
            m[s[j]] = m.get(s[j], 0) + 1
            while any(v > 1 for v in m.values()):
                m[s[i]] -= 1
                if m[s[i]] == 0:
                    del m[s[i]]
                i += 1
            res = max(res, j - i + 1)
        return res
        



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map= set()
        res= 0
        l= 0
        for r in range(len(s)):
            while s[r] in map:
                map.remove(s[l])
                l+= 1
            map.add(s[r])
            res= max(res, r-l+1)
        return res
            
        
