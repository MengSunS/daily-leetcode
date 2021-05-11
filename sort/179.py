class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            if x + y > y + x:
                return 1
            elif x + y < y + x:
                return -1
            else:
                return 0
        
        
        if max(nums) == 0: return '0'
        
        nums = [str(x) for x in nums]
        nums.sort(key = functools.cmp_to_key(compare), reverse=True)
        return "".join(nums)
        
