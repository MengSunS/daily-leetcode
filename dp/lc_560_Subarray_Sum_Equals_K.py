class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map= collections.defaultdict(int)
        map[0]= 1
        sum_acc= 0
        ans= 0
        for i in range(len(nums)):
            sum_acc+= nums[i]
            if sum_acc- k in map:
                ans += map[sum_acc- k]
            map[sum_acc]+= 1
        
        return ans
                
            
        
