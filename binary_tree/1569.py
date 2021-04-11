class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def helper(a):
            if len(a) <= 2: return 1
            left = [i for i in a if i < a[0]]
            right = [i for i in a if i > a[0]]
            return comb(len(left)+len(right), len(left)) * helper(left) * helper(right)
        return (helper(nums) - 1) % (10 ** 9 + 7)
        
