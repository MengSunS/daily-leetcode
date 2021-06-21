# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return 
        if not root.left:
            return self.flatten(root.right)
        self.flatten(root.left)
        self.flatten(root.right)
        h1, h2 = root.left, root.right 
        root.right = h1
        root.left = None
        while h1.right:
            h1 = h1.right
        h1.right = h2
        
        
        
        
