class Solution:
    def balancedString(self, s: str) -> int:
        count = collections.Counter(s)
        i = 0
        n = len(s)
        ret = n-1
        for j, ch in enumerate(s):
            count[ch] -= 1
            while i < n and all(count[c] <= n/4 for c in count):
                ret = min(ret, j-i+1)
                count[s[i]] += 1
                i += 1
        return ret
