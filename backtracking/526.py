# Method 1: 比brute force略微好一点，没直接放进去再检测(O(n!)).这种先检测及时止损O(k), k是所有合格permutation个数 

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

# Method 2: 其实可以放个memo, 大大提升，这个方法是在复习时评论区里的

# 加memo的很不擅长，纯recursion的也不擅长。这题的memo记得是avaialbe set X 有几种方法
#因为btr不是同时进行的，是完成一个深度所有，再另一个分支。前一个到底的已完成了它路上的所有分支，
# 对于与后一个大分支同parent node的下面的是一样的

class Solution:
    def countArrangement(self, N: int) -> int:
        
        def dfs(X):
            if len(X) == 1:
                return 1
            
            if X in cache:
                return cache[X]
            total = 0
            for x in X:
                if x % len(X) == 0 or len(X) % x == 0:
                    total += dfs(X - {x})
                    
            cache[X] = total 
            return total 
        
        cache = {}
        return dfs(frozenset(range(1, N+1)))
    
    
    

   
