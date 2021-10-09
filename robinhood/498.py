class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        cache = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                cache[i + j].append(mat[i][j])
        res = []
        for key in range(m + n - 1):
            if key % 2 == 0:
                res.extend(cache[key][::-1])
            else:
                res.extend(cache[key])
        return res
                
        
