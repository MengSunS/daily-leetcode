#返回word ladder写下backtracking memo版本试一下
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        def dfs(pos, memo):
            if pos == len(s):
                return [[]] #错在了没写bottom up条件
            if pos in memo:
                return memo[pos]
            memo[pos] = []
            for i in range(pos, len(s)):
                if s[pos:i+1] in wordDict:
                    for sub in dfs(i + 1, memo):#若下半段不可分，dfs返回的是[]不是[[]]. for loop不会进行！
                        memo[pos].append([s[pos:i+1]] + sub) #错在了检查每个sub是否为[]
            return memo[pos]
        
        memo = {}
        paths = dfs(0, memo)
        print(memo)
        return [' '.join(l) for l in paths]
                    
            
            
        
