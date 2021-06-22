class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        prefix_sums = list(accumulate([0] + nums + [0]))
        left = []
        res = 0
        for i, h in enumerate(nums + [0]):
            start = i
            while left and h <= left[-1][0]:
                prevH, prevStart = left.pop()
                res = max(res, (prefix_sums[i] - prefix_sums[prevStart]) * prevH)
                start = prevStart
            left.append((h, start))
        return res % (10 ** 9 + 7)
            
            
        
