class Solution:
    """
    @param nums: a non-empty array only positive integers
    @return: true if can partition or false
    """
    def canPartition(self, nums):
        # write your code here
        sum_all= 0
        for i in range(len(nums)):
            sum_all+= nums[i]
        
        if sum_all%2 != 0: return False
        
        half= sum_all//2
        m= len(nums)
        f= [[False]*(half+1) for _ in range(2)]
        f[0][0]= True
        
        for i in range(1, m+1):
            f[i%2][0]= True
            for value in range(1, half+1):
                if nums[i-1]> value:
                    f[i%2][value]= f[(i-1)%2][value]
                else:
                    f[i%2][value]= (f[(i-1)%2][value] or f[(i-1)%2][value- nums[i-1]])
        
        return f[i%2][-1]
