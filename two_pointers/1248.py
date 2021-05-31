# translation: find total number of subarrays that have atMost k sth - atMost k-1 sth. O(n)
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(k):
            res = i = 0
            cnt = 0
            for j in range(n):
                cnt += nums[j] % 2
                while cnt > k:
                    cnt -= nums[i] % 2
                    i += 1
                res += j - i + 1 #出来后(hou)是满足的
            return res
        n = len(nums)
        return atMost(k) - atMost(k - 1)
        
