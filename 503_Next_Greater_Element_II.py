class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n= len(nums)
        res, stack= [-1]*n, []
        
        for i in range(2*n): #maximum case is twice to find all
            while stack and nums[stack[-1]]< nums[i%n]:
                res[stack.pop()]= nums[i%n]
            stack.append(i%n)
        
        return res
        
        
