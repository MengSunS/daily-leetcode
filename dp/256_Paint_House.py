class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp= [[inf]*3 for _ in range(2)]
        dp[0][0]= dp[0][1]=dp[0][2]= 0
        
        for i in range(1, len(costs)+1):
            dp[i%2][0]= min(dp[(i-1)%2][1], dp[(i-1)%2][2])+ costs[i-1][0]
            dp[i%2][1]= min(dp[(i-1)%2][0], dp[(i-1)%2][2])+ costs[i-1][1]
            dp[i%2][2]= min(dp[(i-1)%2][0], dp[(i-1)%2][1])+ costs[i-1][2]
        
        return min(dp[len(costs)%2][0], dp[len(costs)%2][1], dp[len(costs)%2][2])
        
        
