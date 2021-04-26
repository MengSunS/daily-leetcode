class FenwickTree:
    
    def __init__(self, n):
        self.sums = [0] * (n + 1)
    
    def update(self, i, d):
        while i < len(self.sums):
            self.sums[i] += d
            i += i & -i
    
    def query(self, i):
        ans = 0
        while i > 0:
            ans += self.sums[i]
            i -= i & -i
        return ans
        

class Solution:
    def createSortedArray(self, A: List[int]) -> int:
        MOD = 10 ** 9 + 7
        m = max(A) # lee神可以做的原因是本题所有element均 >= 1, 1649题就不能这么做
        ft = FenwickTree(max(A))
        cnt = 0
        for x in A:
            cnt += min(ft.query(x - 1), ft.query(m) - ft.query(x))
            ft.update(x, 1)
        return cnt % MOD
            
            
        
# Method 2: mine, ranks of sorted set, if some elements < 0 still correct 

class FenwickTree:
    
    def __init__(self, n):
        self.sums = [0] * (n + 1)
    
    def update(self, i, d):
        while i < len(self.sums):
            self.sums[i] += d
            i += i & -i
    
    def query(self, i):
        ans = 0
        while i > 0:
            ans += self.sums[i]
            i -= i & -i
        return ans
        

class Solution:
    def createSortedArray(self, A: List[int]) -> int:
        MOD = 10 ** 9 + 7
        sortedsetA = sorted(set(A))
        ranks = {val: i + 1 for i, val in enumerate(sortedsetA)}   
        ft = FenwickTree(len(ranks))
        cost = 0
        for x in A:
            cost += min(ft.query(bisect.bisect(sortedsetA, x - 1)), ft.query(len(ranks)) - ft.query(ranks[x]))
            ft.update(ranks[x], 1)
        return cost % MOD        
