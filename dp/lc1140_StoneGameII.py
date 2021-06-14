class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        if not piles:
            return 
        memo= {}
        self.dfs(piles, 0, 1, memo)
        
        return int((sum(piles)+memo[0, 1])/2)
        
    
    def dfs(self, piles, index, M, memo):
        if (index, M) in memo:
            return memo[index, M]
        if len(piles)-index<= 2*M:
            memo[(index, M)]= sum(piles[index:])
            return memo[(index, M)]
        
        if index> len(piles):
            return 0
        
        max_diff= -sys.maxsize
        for x in range(1, 2*M+1):
            max_diff= max(max_diff, sum(piles[index:index+x])- self.dfs(piles, index+x, max(x, M), memo))
        memo[index, M]= max_diff
        return memo[index, M]
        
