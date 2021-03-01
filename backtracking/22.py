class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # top down 1 dim dp, j inside, i-j-1 outside
        # '(x) y' where a and y are combinations of brackets of that size and x+ y= n-1
        # so (j)k with j+k= i-1
        dp= [[] for _ in range(n+1)]
        dp[0].append('')
        
        for i in range(n+1):
            for j in range(i):
                dp[i]+= ['('+ x+ ')' + y for x in dp[j] for y in dp[i-j-1]]
        return dp[n]
        
        
