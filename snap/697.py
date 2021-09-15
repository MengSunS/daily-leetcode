class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = collections.Counter(nums)
        f_max = max(freq.values())
        keys = set([k for k, f in freq.items() if f == f_max])
        first, last = {}, {}
        res = len(nums)
        for i, a in enumerate(nums):
            if a in keys:
                first.setdefault(a, i)
                last[a] = i
        for k in keys:
            res = min(res, last[k] - first[k] + 1)
        return res
            
        
        
        
