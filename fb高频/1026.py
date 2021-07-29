class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(node, min_val, max_val):
            if not node:
                self.res = max(self.res, max_val - min_val)
                return 
            dfs(node.left, min(min_val, node.val), max(max_val, node.val))
            dfs(node.right, min(min_val, node.val), max(max_val, node.val))
        
        self.res = 0
        dfs(root, 10 ** 5, 0)
        return self.res
    
    # 默默的backtracking 
