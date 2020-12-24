class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        map= {}
        l= 0
        res= 0
        for r in range(len(s)):
            map[s[r]]= map.get(s[r], 0)+ 1
            while len(map)> k:
                map[s[l]]-= 1
                if map[s[l]]==0:
                    del map[s[l]]
                l+= 1
            res= max(res, r-l+1)
        return res
        
