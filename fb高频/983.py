class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [float('inf') for _ in range(days[-1] + 1)]
        dp[0] = 0
        go = set(days)
        for day in range(1, days[-1] + 1):
            if day not in go:
                dp[day] = dp[day - 1]
            else:
                a = dp[max(0, day - 1)] + costs[0]
                b = dp[max(0, day - 7)] + costs[1]
                c = dp[max(0, day - 30)] + costs[2]
                dp[day] = min(a, b,c)
        return dp[-1]
                
            
