class Solution(object):
    def pathSum(self, nums):
        values = {}
        for num in nums:
            d, p, v = num // 100, num // 10 % 10, num % 10
            values[(d, p)] = v
        
        def dfs(node, path_sum):
            if node not in values:  
                return
            
            path_sum += values[node] 
            d, p = node
            left, right = (d + 1, p * 2 - 1), (d + 1, p * 2)
            if left not in values and right not in values:
                self.res += path_sum
            
            dfs(left, path_sum)
            dfs(right, path_sum)
            path_sum -= values[node]                            
        
        
        root = (nums[0] // 100, nums[0] // 10 % 10) 
        self.res = 0
        dfs(root, 0)
        return self.res
