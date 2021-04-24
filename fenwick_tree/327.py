# O(nlogn)
# fenwick tree is freq of presums, order is sorted(presum), so rank + 1 is the index in array.
# bisect in sortedSums finds the rank/index directly 

import bisect

class FenwickTree:
    def __init__(self, n) -> None:
        self.sums = [0] * (n+1)
    
    def query(self, i) -> int:
        ans = 0
        while i > 0:
            ans += self.sums[i]
            i -= i & -i
        return ans
    
    def update(self, i, delta) -> None:
        while i < len(self.sums):
            self.sums[i] += delta
            i += i & -i
            
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        presums = [0] * (len(nums)+1)
        for i, val in enumerate(nums):
            presums[i+1] = presums[i] + val
        sortedSums = sorted(presums)
        ranks = {s: i for i, s in enumerate(sortedSums)}
        ft = FenwickTree(len(presums))
        res = 0
        for val in presums:
            res += (ft.query(bisect.bisect_right(sortedSums, val - lower)) -
                   ft.query(bisect.bisect_left(sortedSums, val - upper)))
            ft.update(ranks[val] + 1, 1)
        return res
