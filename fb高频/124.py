# time O(N), each node process no more than twice? space O(H)

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        def singlePathSum(node):
            if node is None:
                return 0
            if not node.left and not node.right:
                self.res = max(self.res, node.val)
                return node.val
            l = singlePathSum(node.left)
            r = singlePathSum(node.right)
            left = max(l, 0)
            right = max(r, 0)
            self.res = max(self.res, left + right + node.val)
            return max(left, right) + node.val
        
        singlePathSum(root)
        return self.res
            
