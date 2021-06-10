class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if nums[0] >= n: return n
        for i in range(n):
            if nums[i] >= n - i and nums[i - 1] < n - i:
                return n - i
        return -1
    #想成h index比较intuitive一点
            
        
