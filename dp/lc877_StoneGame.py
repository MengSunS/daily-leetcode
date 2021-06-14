------dfs+memo---

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        if not piles:
            return 
        memo= {}
        return self.dfs(piles, 0, len(piles)-1, memo)
    
    def dfs(self, piles, left, right, memo):
        if (left, right) in memo:
            return memo[left, right]
        if left==right:
            return piles[left]
        
       
        memo[left, right]= max(piles[left]+ self.dfs(piles, left+1, right, memo), piles[right]+ self.dfs(piles, left, right-1, memo))
        return memo[left, right]
        
        
