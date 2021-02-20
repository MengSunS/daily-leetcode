class Solution:
    def countArrangement(self, n: int) -> int:
        def dfs(visited, pos):
            if pos== n+1:
                self.res += 1
                return

            for i in range(1, n+1):
                if visited[i]:
                    continue
                if i % pos == 0 or pos % i == 0:
                    visited[i]= 1
                    dfs(visited, pos + 1)
                    visited[i]= 0
        
        self.res= 0
        visited= [0]* (n+1)
        dfs(visited, 1)
        return self.res
    
    
    

   
