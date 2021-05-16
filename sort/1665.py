class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0])
        res = 0
        for a, m in tasks:
            res = max(res + a, m)
        return res
    
    
    
