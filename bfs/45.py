class Solution:
    def jump(self, nums: List[int]) -> int:
        start, end= 0, 0
        if len(nums)==1: return 0
        n= len(nums)
        step= 0
        while start<= end:
            new_end= end
            while start<= end:
                new_end= max(new_end, start+ nums[start])
                if new_end>= n- 1:
                    return step+ 1
                start+= 1
            start= end+1
            end= new_end
            step+= 1
        # 变相bfs,不需要真的把这区间的next candidates全放进去，会超时，这里是因为next candidates区间的是连续的，只需要记个首尾表示一下
            
        
