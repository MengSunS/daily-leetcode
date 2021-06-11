class Fenwick:
    def __init__(self, n):
        self.A = [0] * (n + 1)
    
    def add(self, i, delta):
        while i < len(self.A):
            self.A[i] += delta
            i += i & (-i) # lowbit: i & (-i)
    
    def query(self, i):
        ans = 0
        while i > 0:
            ans += self.A[i]
            i -= i & (-i)
        return ans


class MKAverage:

    def __init__(self, m: int, k: int):
        self.stream = deque()
        self.m, self.k = m, k
        self.val, self.idx = Fenwick(10 ** 5),  Fenwick(10 ** 5)
        

    def addElement(self, num: int) -> None:
        self.stream.append(num)
        self.val.add(num, num)
        self.idx.add(num, 1)
        if len(self.stream) > self.m:
            num = self.stream.popleft()
            self.val.add(num, -num)
            self.idx.add(num, -1)
    
    def bsearch(self, target):
        l, r = 0, 10 **5 + 1
        while l < r:
            mid = l + (r - l) // 2
            if self.idx.query(mid) < target:
                l = mid + 1
            else:
                r = mid
        return l
                       

    def calculateMKAverage(self) -> int:
        if len(self.stream) < self.m: return -1
        lo, hi = self.bsearch(self.k), self.bsearch(self.m - self.k)
        res = self.val.query(hi) - self.val.query(lo)
        res += (self.idx.query(lo) - self.k) * lo
        res -= (self.idx.query(hi) - (self.m - self.k)) * hi
        return res // (self.m - 2 * self.k)
        


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
