# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
         
        def dfs(root, preSum):
            if root:
                preSum += root.val
                self.res += cache.get(preSum - targetSum, 0) 
                cache[preSum] = cache.get(preSum, 0) + 1      
                dfs(root.left, preSum)
                dfs(root.right, preSum)
                cache[preSum] -= 1
                
        self.res = 0
        cache = {0: 1}
        dfs(root, 0)
        return self.res
                
        
