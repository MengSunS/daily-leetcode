class Fenwick:
    def __init__(self, n):
        self.sums = [0] *(n + 1)
    
    def query(self, i):
        sums = 0
        while i > 0:
            sums += self.sums[i]
            i -= i & -i
        return sums
    
    def update(self, i, d):
        while i < len(self.sums):
            self.sums[i] += d
            i += i & -i
            
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        ranks = {val: i + 1 for i, val in enumerate(sorted(set(nums)))}
        sortedNums = sorted(set(nums))
        ft = Fenwick(len(ranks))
        res = 0
        for j in range(len(nums)):
            res += (ft.query(len(ranks)) - ft.query(bisect.bisect_right(sortedNums, nums[j]*2)))
            ft.update(ranks[nums[j]], 1)
        return res
        
        
