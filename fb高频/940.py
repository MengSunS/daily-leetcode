class Solution:
    def distinctSubseqII(self, s: str) -> int:
        end = [0] *26
        for ch in s:
            end[ord(ch) - ord('a')] = sum(end) + 1
        return sum(end) % (10 ** 9 + 7)
                



class Solution:
    def distinctSubseqII(self, s: str) -> int:
        s = '#' + s
        n = len(s)
        dp = [0] * n
        dp[0] = 1
        M = 10 ** 9 + 7
        last = {}
        for i in range(1, n):
            dp[i] = 2 * dp[i - 1] % M
            if s[i] in seen:
                dp[i] = (dp[i] - dp[last[s[i]] - 1]) % M
            last[s[i]] = i
        return dp[-1] - 1        
