# Dijkstra, 
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])
        vals = sum([row[0] for row in mat])
        hp = [(vals, [0] * m)]
        seen = set(tuple([0] * m))
        res = []
        
        while len(res) < k:
            s, idx_lst = heapq.heappop(hp)
            res.append(s)
            for i in range(m):
                new_idx_lst = list(idx_lst)
                new_idx_lst[i] += 1
                if new_idx_lst[i] < n and tuple(new_idx_lst) not in seen:
                    seen.add(tuple(new_idx_lst))
                    heapq.heappush(hp, (s + mat[i][new_idx_lst[i]] - mat[i][idx_lst[i]], new_idx_lst))
        return res[-1]
                
        
        
