class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(x, path, col, diag1, diag2):
            if x== n:
                res.append(path[:])
                return 
            
            for y in range(n):
                if y in col or (y+x) in diag1 or (y-x) in diag2:
                    continue
                col.add(y)
                diag1.add(y+x)
                diag2.add(y-x)
                dfs(x+ 1, path+ ['.'* y + 'Q'+ '.'* (n-y-1)], col, diag1, diag2)
                col.remove(y)
                diag1.remove(y+x)
                diag2.remove(y-x)
                
       
        res= []
        col, diag1, diag2= set(), set(), set()
        dfs(0, [], col, diag1, diag2)
        return res
    
    # need 3 sets to record visited cuz, other lines y+x might equal to current points y-x, deleting the wrong one
    # x+y= b, y-x= b. 对角线上的所有点满足且只有对角线上的点(x, y)满足==b 这个条件
        
        
                
                
                
                
        
