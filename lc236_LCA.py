# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', A: 'TreeNode', B: 'TreeNode') -> 'TreeNode':
        if not root:
            return 
        
        if root==A or root==B:
            return root
        
        left= self.lowestCommonAncestor(root.left, A, B)
        right= self.lowestCommonAncestor(root.right, A, B)
        

        if left and right:
            return root
        if left:
            return left
        if right:
            return right
        
