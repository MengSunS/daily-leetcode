class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]: 
        def dfs(path, index, seen):
            if len(seen) == n:
                return path[:]
    
            for nxt in range(n, 0, -1):
                if nxt in seen:
                    continue
                while index < m and path[index] != 0:
                    index += 1
                if nxt == 1:
                    path[index] = 1
                    seen.add(nxt)
                    res = dfs(path, index + 1, seen)
                    if res:
                        return res
                    path[index] = 0
                    seen.remove(nxt)
                else:
                    if index + nxt >= m or path[index + nxt] != 0:
                        continue
                    else: 
                        path[index] = path[index + nxt] = nxt
                        seen.add(nxt)
                        if dfs(path, index + 1, seen):
                            return path[:]
                        path[index] = path[index + nxt] = 0
                        seen.remove(nxt)
            return False
                        
        m = 1 + (n - 1) * 2
        path = [0] * m
        res = []
        seen = set()            
        return dfs(path, 0, seen)
       
                        
                    
                
