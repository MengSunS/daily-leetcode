hardest part is the translation: find longest subarray with atMost K 0s.

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = i = 0
        n = len(nums)
        zeros = 0
        for j in range(n):
            zeros += (nums[j] == 0)
            while zeros > k:
                zeros -= (nums[i] == 0)
                i += 1
            res = max(res, j - i + 1)
        return res
    
# no need to keep tarck of res, instead, j ,i are not the corrspoding index, but the j - i + 1 is the 
window size. when okay, try to expand j, when exceed, move i, j together, till j hits the end.       
                
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = i = 0
        n = len(nums)
        zeros = 0
        for j in range(n):
            zeros += (nums[j] == 0)
            if zeros > k:
                zeros -= (nums[i] == 0)
                i += 1
        return j - i + 1
    
       
                
                
