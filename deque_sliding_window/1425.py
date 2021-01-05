# https://www.youtube.com/watch?v=FSbFPH7ejHk

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n= len(nums)
        dp= [0]*n
        q= collections.deque([])
        res= -sys.maxsize
        for j in range(n):  
            # 一定先把前面越界的储存pop掉
            while q and q[0]+ k< j:
                q.popleft()
                
            dp[j]= nums[j]
            if q:
                dp[j]= max(dp[j], dp[q[0]]+ nums[j])
            res= max(res, dp[j])
            
            while q and dp[j]>= dp[q[-1]]:
                q.pop()
            q.append(j)
        return res
