--------method 1: dp bottom up--------

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp= [float('-inf')]*(len(stoneValue))+ [0]
        
        for i in range(len(stoneValue)-1, -1, -1):
            target_sum= 0
            for j in range(0, 3):
                if i+j== len(stoneValue):
                    break
                target_sum+= stoneValue[i+j]
                dp[i]= max(dp[i], target_sum- dp[i+j+1])
        
        if dp[0]> 0: return 'Alice'
        elif dp[0]< 0: return 'Bob'
        return 'Tie'

------method 2: dfs+memo------------

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        if not stoneValue: return 
        
        memo= {}
        self.dfs(stoneValue, 0, memo)
        
        if memo[0]> 0: return 'Alice'
        elif memo[0]< 0:
            return 'Bob'
        return 'Tie'
    
    def dfs(self, stoneValue, index, memo):
        if index in memo: return memo[index]
        if index>= len(stoneValue): return 0
        
        
        
        diff_max= -sys.maxsize
        for m in [1,2,3]:
            
                diff_max= max(diff_max, sum(stoneValue[index:index+m])- self.dfs(stoneValue, index+m, memo))
                
        memo[index]= diff_max
        return memo[index]        
