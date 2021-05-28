class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        sign = {1 : -1}
        n = len(nums)
        res = 0
        prefix = 1
        for i in range(n):
            if nums[i] > 0: prefix *= 1
            elif nums[i] < 0: prefix *= -1
            else: prefix = 0
                    
            if prefix == 0:
                sign = {1 : i}
                prefix = 1
                continue
            if prefix in sign:
                res = max(res, i - sign[prefix])
            else:
                sign[prefix] = i
        return res
