class Solution:
    def minAvailableDuration(self, A: List[List[int]], B: List[List[int]], k: int) -> List[int]:
        C = list(filter(lambda x: x[1] - x[0] >= k, A + B))
        C.sort()
        if not C: return []
        n = len(C)
        last_end = C[0][1]
        
        for i in range(1, n):
            if C[i][0] + k <= last_end:
                return [C[i][0], C[i][0] + k]
            if C[i][1] >= last_end:
                last_end = C[i][1]
        return []
            
        
            
        
