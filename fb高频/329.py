#这种返回最长（可能有限制）路径，特别是只返回一个数的（本题长度），要本能反应是dp,想清楚如果下一个以前计算过的话，目前这个跟下一个什么关系。这样就自然的是dfs式的top down dp. 带memo的dfs就是dp. 注意memo里记录的input中的(x, y)的ans, 所以绝对是在for loop之后的外面，那么for loop里面ans是取最大还是什么操作，就是dp的关键，input (x, y)层和下一层结果的关系怎么计算连接。还是就是ans初始值赋值什么，不走循环应该返回什么，必须走循环就走循环最后一个返回什么，注意检查一下。这道题还有就是memo放在主函数的for loop外面，如果传入dp的是{},那么没有完全记忆化，因为对于一个点，只要做了dfs,就尝试了所有路径长度。

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        def dp(i, j, memo):
            if (i, j) in memo:
                return memo[(i, j)]
            ans = 1 #不走循环时是什么值，但这里不可能不走循环，走循环
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if ni >= m or ni < 0 or nj >= n or nj < 0 or matrix[ni][nj] <= matrix[i][j]:
                    continue
                ans = max(ans, dp(ni, nj, memo) + 1) #取max, 下层结果跟这层结果什么计算连接
            memo[(i, j)] = ans #memo记得是输入的x, y,而非循环里面的ni, nj
            return ans
        
        m, n = len(matrix), len(matrix[0])
        res = 0
        memo = {}
        for i in range(m):
            for j in range(n):
                res = max(res, dp(i, j, memo)) #这里不要放{},没有完全记忆化
        return res
                    
       

#推荐写法 decorator不容易出错，本题的话比如memo不要传{},要写在最外面啦，memo记录的是input中的(x, y)而非下一层的，所以要放在dp for loop后面的外面啦。这些都死因为自己写memo写出的bug或不够优化。

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        @lru_cache(None)
        def dp(i, j):
            ans = 1
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if ni >= m or ni < 0 or nj >= n or nj < 0 or matrix[ni][nj] <= matrix[i][j]:
                    continue
                ans = max(ans, dp(ni, nj) + 1)
            return ans
        
        m, n = len(matrix), len(matrix[0])
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dp(i, j))
        return res
                    
         
