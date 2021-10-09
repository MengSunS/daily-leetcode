class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        M = [[0] * n for _ in range(n)]
        M[0][0] = 1
        dx, dy = 0, 1
        x, y = 0, 0
        num = 1
        
        while num < n ** 2:
            while 0 <= x + dx < n and 0 <= y + dy < n and M[x + dx][y + dy] == 0:
                x += dx
                y += dy
                num += 1
                M[x][y] = num
            dx, dy = -dy, dx
        return M
        
