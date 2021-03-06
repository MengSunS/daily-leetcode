# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes= set(nodes)
        def dfs(root):
            if not root:
                return 
            if root in nodes:
                return root

            left= self.lowestCommonAncestor(root.left, nodes)
            right= self.lowestCommonAncestor(root.right, nodes)

            if left and right:
                return root
            return left or right
        
        return dfs(root)
        
          
    
