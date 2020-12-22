# Method 1: map, a nothworthy point is when sum(all)==target, for loop does not cover, need corner case check

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target= sum(nums)- x
        if target==0: return len(nums)
        preSum= 0
        map= {0:-1}
        res= -1
        
        for r in range(len(nums)):
            preSum+= nums[r]
            if preSum- target in map:
                res= max(res, r- map[preSum-target])
                
            map[preSum]= r
           
            
        return len(nums)- res if res>=0 else -1

# Method 2: 2 pointers, 我认为这种方法只适用于全是正数

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target= sum(nums)- x
        n= len(nums)
        preSum= 0
        l= 0
        length= -1
        for r in range(n):
            preSum+= nums[r]
            while l< n and preSum> target:
                preSum-= nums[l]
                l+= 1
            if preSum== target:
                length= max(length, r-l+1)
        return n- length if length>= 0 else -1
