class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def dfs(i, col, diag, adiag):
            if i== n:
                self.res+= 1
                return 
            for j in range(n):
                if j in col or (i+j) in diag or (j-i) in adiag:
                    continue
                col.add(j)
                diag.add(i+j)
                adiag.add(j-i)
                dfs(i+1, col, diag, adiag)
                col.remove(j)
                diag.remove(i+j)
                adiag.remove(j-i)
        self.res= 0
        col, diag, adiag= set(), set(), set()
        dfs(0, col, diag, adiag)
        return self.res
                
        
