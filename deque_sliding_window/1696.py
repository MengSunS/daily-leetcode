class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        q= collections.deque([(nums[0], 0)])
        
        for i in range(1, len(nums)):
            if q and q[0][1]== i-k-1:
                q.popleft()
            curStep= q[0][0]+ nums[i]
            while q and q[-1][0]< curStep:
                q.pop()
            q.append((curStep, i))
            
        return q[-1][0]
            
        # dp[i]= max(dp[i-k], dp[i-k+1], ...dp[i-1])+ nums[i]
        # max() there is a large portion of overlap when slding teh window,
        # optimize this max () part by sliding window maximum.
        # whats put in the deque is max(window)+ nums[i], this is the different part
        # no need to create a dp array, just refer to the top of the deque.
        
        
        # https://www.youtube.com/watch?v=f4fEdD0IbEc        
        
