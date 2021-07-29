class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        
        @lru_cache(None)
        def dfs(state):
            if state == 0:
                return 0
            
            remain = [i for i in range(n) if state & (1 << i)]
            index = itertools.combinations(remain, size)
            res = float('inf')
            for idx in list(index):
                group = [nums[-i - 1] for i in idx]
                if len(set(group)) < size:
                    continue
                    
                newState = state
                for i in idx:
                    newState ^= (1 << i)
                res = min(res, max(group) - min(group) + dfs(newState))
            return res
        
        n = len(nums)
        size = n // k
        return dfs(2 ** n - 1) if dfs(2 ** n - 1) != float('inf') else -1
                
        
