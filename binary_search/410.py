class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def check(nums, target, n):
            curSum, cnt = 0, 1
            for num in nums:
                curSum += num
                if curSum > target:
                    curSum = num
                    cnt += 1
                    if cnt > n:
                        return False
            return True
        
        l, r = max(nums), sum(nums)
        if m == 1:
            return r
        while l < r:
            mid = l + (r - l) // 2
            if check(nums, mid, m):
                r = mid 
            else:
                l = mid + 1
        return l
        
            
        
