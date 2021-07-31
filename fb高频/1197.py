class Solution:
    @lru_cache(None)
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        if x + y == 2:
            return 2
        elif x + y == 0:
            return 0
        return min(self.minKnightMoves(x - 1, y - 2), self.minKnightMoves(x - 2, y - 1)) + 1
    
        
