def winnerSquareGame(self, n: int) -> bool:
        memo= {}
        return self.dfs(n, memo)
        
    
    def dfs(self, n, memo):
        if n in memo:
            return memo[n]
        
        # if int(sqrt(n))**2== n:
        #     memo[n]= True
        #     return memo[n]
        
        if n==1:
            memo[n]= True
            return memo[n]
        
        can_win= False
        for i in range(1, int(sqrt(n))+1):
            can_win= can_win or not self.dfs(n-i**2, memo)
        memo[n]= can_win
        
        return memo[n]
