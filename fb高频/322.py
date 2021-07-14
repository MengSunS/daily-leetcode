class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i]: 凑成i amount至少需要多少硬币
        dp = [0] + [float('inf')] * amount
        for i in range(1, amount + 1):
            dp[i] = min([dp[i - coin] if coin <= i else float('inf') for coin in coins]) + 1
        return dp[amount] if dp[amount] != float('inf') else -1
        
