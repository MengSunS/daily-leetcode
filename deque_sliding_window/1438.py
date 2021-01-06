class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # 主体是个双指针，里面包着deque sliding window maximum;
        # lc1425主体是个dp,里面包着deque sliding window maximum
        i= 0
        dq_max, dq_min= collections.deque(), collections.deque()
        n= len(nums)
        res= 0
        for j in range(n):
            while dq_max and nums[dq_max[-1]]<= nums[j]:
                dq_max.pop()
            while dq_min and nums[dq_min[-1]]>= nums[j]:
                dq_min.pop()
            dq_max.append(j)
            dq_min.append(j)
            while dq_max and dq_min and abs(nums[dq_max[0]]- nums[dq_min[0]])> limit:
                while dq_max and dq_max[0]<= i:
                    dq_max.popleft()
                while dq_min and dq_min[0]<= i:
                    dq_min.popleft()
                i+= 1
            res= max(res, j-i+1)
        return res
            
                
                
        
