class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s, i = 0, 0
        n = len(nums)
        res = inf
        for j in range(n):
            s += nums[j]
            while s >= target:
                res = min(res, j - i + 1)
                s -= nums[i]
                i += 1
                
        return res if res != inf else 0
                
        
# 209 follow-up: 862. what if the numbers can be negative? monostack
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        dq = collections.deque([(0, -1)])
        n = len(nums)
        s = 0
        res = n + 1
        for j in range(n):
            s += nums[j]
            while dq and dq[0][0] <= s - k:
                res = min(res, j - dq.popleft()[1])
            while dq and dq[-1][0] >= s:
                dq.pop()
            dq.append((s, j))
        return res if res != n + 1 else -1
            
        
                
