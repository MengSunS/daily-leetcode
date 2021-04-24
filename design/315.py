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
    def countSmaller(self, nums: List[int]) -> List[int]:
        rank = {v: i for i, v in enumerate(sorted(set(nums)))}
        tree = FenwickTree(len(rank))
        res = []
        for i in range(len(nums) - 1, -1, -1):
            res.append(tree.query(rank[nums[i]]))
            tree.update(rank[nums[i]] + 1, 1)
        return res[::-1]
            
        
