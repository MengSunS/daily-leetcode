class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q = collections.deque([(i + 1, j, 1), (i, j + 1, 1), (i - 1, j, 1), (i, j - 1, 1)])
                    while q:
                        
                        x, y, step = q.popleft()
                        if x >= m or x < 0 or y >= n or y < 0 or rooms[x][y] in [0, -1] or rooms[x][y] <= step: 
                            continue
                        
                        rooms[x][y] = step
                        q.extend([(x + 1, y, step + 1), (x, y + 1, step + 1), (x - 1, y, step + 1), (x, y - 1, step + 1)])
                        
                        

        
