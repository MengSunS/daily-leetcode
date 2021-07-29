class UnionFind:
    def __init__(self, n):
        self.arr = {(i, j, k) : (i, j, k) for i in range(n) for j in range(n) for k in range(4)}
        self.res = n * n * 4
    def union(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx != fy:
            self.arr[fx] = fy
            self.res -= 1
    def find(self, x):
        if self.arr[x] != x:
            self.arr[x] = self.find(self.arr[x])
        return self.arr[x]
        # i = x
        # while self.arr[i] != i:
        #     i = self.arr[i]
        # while x != i:
        #     tmp = self.arr[x]
        #     self.arr[x] = i
        #     x = tmp
        # return x
        
        

class Solution:
    def regionsBySlashes(self, A: List[str]) -> int:
        n = len(A)
        UF = UnionFind(n)
        for i in range(n):
            for j in range(n):
                if A[i][j] != '\\':
                    UF.union((i, j, 0), (i, j, 1))
                    UF.union((i, j, 2), (i, j, 3))
                if A[i][j] != '/':
                    UF.union((i, j, 0), (i, j, 2)) 
                    UF.union((i, j, 1), (i, j, 3))
                     
                if i + 1 < n:
                    UF.union((i, j, 3), (i + 1, j, 0))
                if j + 1 < n:
                    UF.union((i, j, 2), (i, j + 1, 1))
        return UF.res
