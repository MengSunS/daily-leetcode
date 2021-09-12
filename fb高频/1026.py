# top down
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

# bottom up

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node):
            if not node:
                return float('inf'), float('-inf')
            l_min, l_max = dfs(node.left)
            r_min, r_max = dfs(node.right)
            self.res = max(self.res, node.val - min(l_min, r_min), max(l_max, r_max) - node.val)
            return min(l_min, r_min, node.val), max(l_max, r_max, node.val)
        
        dfs(root)
        return self.res
