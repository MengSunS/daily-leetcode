# recursively call the function itself

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val> root.val and q.val> root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val< root.val and q.val< root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

# iterative

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val> root.val and q.val> root.val:
                root= root.right
            elif p.val< root.val and q.val< root.val:
                root= root.left
            else:
                return root        
