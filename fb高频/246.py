class Solution:
    def isStrobogrammatic(self, nums: str) -> bool:
        
        match = set([('6', '9'), ('9', '6'), ('8', '8'), ('1', '1'), ('0', '0')])
        i, j = 0, len(nums) - 1
        while i <= j:
            if (nums[i], nums[j]) not in match:
                return False
            i += 1
            j -= 1
        return True
        
        
        
