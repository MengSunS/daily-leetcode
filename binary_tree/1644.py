# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p_find, self.q_find= False, False
        res= self.dfs(root, p, q)
       
        return res if (self.p_find and self.q_find) else None
        
    def dfs(self, root, p, q):
        if not root:
            return 
        
        left= self.dfs(root.left, p, q)
        right= self.dfs(root.right, p, q)
        
        if root==p:
            self.p_find= True
            return root
        if root==q:
            self.q_find= True
            return root
        
        
        if left and right:
            return root
        return left or right
        
