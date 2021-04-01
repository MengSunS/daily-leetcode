class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        l, r = max(nums), sum(nums)
        if m == 1:
            return r
        while l < r:
            mid = l + (r - l) // 2
            cnt, curSum = 1, 0
            for num in nums:
                if curSum + num > mid:
                    cnt += 1
                    curSum = 0
                curSum += num
            if cnt > m:
                l = mid + 1
            else:
                r = mid
        return l
        
            
        
