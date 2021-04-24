# Fenwick tree, aka, Binary index tree
class BIT2D:
    def __init__(self, n1: int, n2: int):
        self.n1 = n1
        self.n2 = n2
        self._tree = [[0] * (n2 + 1) for _ in range(n1 + 1)]

    def add(self, i: int, j: int, delta: int):
        i_lst, j_lst = [], []
        while i <= self.n1:
            i_lst.append(i)
            i += i & -i
        while j <= self.n2:
            j_lst.append(j)
            j += j & -j
        for ii in i_lst:
            for jj in j_lst:
                self._tree[ii][jj] += delta

    def query(self, i: int, j: int) -> int:
        i_lst, j_lst = [], []
        while i > 0:
            i_lst.append(i)
            i -= i & -i
        while j > 0:
            j_lst.append(j)
            j -= j & -j
        ans = 0
        for ii in i_lst:
            for jj in j_lst:
                ans += self._tree[ii][jj]
        return ans


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        if not self.matrix or not self.matrix[0]:
            n1, n2 = 0, 0
        else:
            n1, n2 = len(self.matrix), len(self.matrix[0])
        self.BIT2D = BIT2D(n1, n2)
        for i in range(n1):
            for j in range(n2):
                self.BIT2D.add(i + 1, j + 1, self.matrix[i][j])

    def update(self, row: int, col: int, val: int) -> None:
        self.BIT2D.add(row + 1, col + 1, val - self.matrix[row][col])
        self.matrix[row][col] = val

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, row2, col1, col2 = row1 + 1, row2 + 1, col1 + 1, col2 +1
        return self.BIT2D.query(row2, col2) - self.BIT2D.query(row2, col1 - 1) - self.BIT2D.query(row1 - 1, col2) + self.BIT2D.query(row1 - 1, col1 - 1)
        
    
