class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        visited= set()
        self.res= -inf
        path= []
        self.dfs(s, path, visited)
        
        return self.res
      
    def dfs(self, s, path, visited):
        if s=='':
            self.res= max(self.res, len(path))
            return 
            
        for i in range(1, len(s)+1):
            slice= s[:i]
            # 这个len(path)+len(s)> self.res prune的地方提速很重要
            if slice not in visited and len(path)+len(s)> self.res:
                visited.add(slice)
                path.append(slice)
                self.dfs(s[i:], path, visited)
                path.pop()
                visited.remove(slice)
        
        
