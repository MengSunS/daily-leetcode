# method 1: bottom-up dp

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        res = -1
        for word in sorted(words, key=len):
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]
                dp[word] = max(dp.get(prev, 0) + 1, dp.get(word, 0))
                res = max(res, dp[word])
        return res




#method 2: top-down dp

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        @lru_cache(None)
        def dp(word):
            res = 1
            for i in range(len(word)):
                prev = word[:i] + word[i+1:]
                if prev in wordSet:
                    res = max(res, dp(prev) + 1)
            return res
        
        wordSet = set(words)
        # words.sort(key=len)
        return max(dp(word) for word in words)
                    
        
