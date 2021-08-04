class Solution:
    def spiralMatrixIII(self, R: int, C: int, x: int, y: int) -> List[List[int]]:
        res = []
        k, count = 0, 0
        dx, dy = 0, 1
        while count < R * C:
            for i in range(k // 2 + 1):
                if 0 <= x < R and 0 <= y < C:
                    res.append([x, y])
                    count += 1
                x, y = x + dx, y + dy
            dx, dy = dy, -dx
            k += 1
        return res
    
        
