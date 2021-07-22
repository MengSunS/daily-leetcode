class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return -1
            
            l = dfs(root.left)
            r = dfs(root.right)
            self.res = max(self.res, l + r + 2)
            return max(l, r) + 1
        
        self.res = 0
        dfs(root)
        return self.res
        
