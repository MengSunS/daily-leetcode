# method 1: 


# Pigeonhole principle
#     12 3        89   8//4 = 2 这5个数均匀分布的时候gap是多少，每个鸽子占一个格，不均匀分布时，有些鸽子在一个格子里; 8//2 + 1= 5
#     -- -- -- -- --   
 
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: 
            return 0
        mini, maxi = min(nums), max(nums)
        b = max(1, (maxi - mini) // (n - 1)) # bucket size
        k = (maxi - mini) // b + 1 #额外多几个格子也没关系
        buckets = [[inf, -inf] for _ in range(k)]
        for num in nums:
            idx = (num - mini) // b
            x, y = buckets[idx]
            buckets[idx] = [min(x, num), max(y, num)]
        
        prev = mini
        res = 0
        for x, y in buckets:
            if x != inf:
                res = max(res, x - prev)
                prev = y
        return res
                

# mehod 2: radix sort 

# radix sort, time complexity O(m*n), m is number of digits in maximim num within nums, n is length of nums.
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        buckets = [[] for _ in range(10)]
        maxi = max(nums)
        exp = 1
        while maxi // exp > 0:
            for num in nums:
                idx = num // exp % 10 
                buckets[idx].append(num)
            nums = []
            for b in buckets:
                nums += b
            buckets = [[] for _ in range(10)]
            exp *= 10
        
        res = 0
        for i in range(1, len(nums)):
            res = max(res, nums[i] - nums[i-1])
        return res
            
        
