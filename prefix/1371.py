class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4 }
        seen = [-1] + [inf] * (2**5)
        res, n, cur = 0, len(s), 0
        for i, ch in enumerate(s):
            if ch in vowels:
                cur ^= (1 << vowels[ch])
            res = max(res, i - seen[cur])
            seen[cur] = min(seen[cur], i)
        return res



class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        res, cur = 0, 0
        seen = {0 : -1} # 0 is for all even
        for i, c in enumerate(s):
            if c in vowels:
                cur ^= 1 << vowels[c]
            # if cur in seen:
            #     res = max(res, i - seen[cur])
            # else:
            #     seen[cur] = i
            seen.setdefault(cur, i)
            res = max(res, i - seen[cur])
        return res
        
