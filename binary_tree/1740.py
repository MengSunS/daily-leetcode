# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        def find_lca(root):
            if not root:
                return 
            if root.val==p or root.val==q:
                return root
            left= find_lca(root.left)
            right= find_lca(root.right)
            if left and right:
                return root
            return left or right
        
        def dist(node, target):
            if not node:
                return inf
            if node.val==target:
                return 0
            left= dist(node.left, target)
            right= dist(node.right, target)
            return min(left, right)+ 1
        
        
        lca= find_lca(root)
        return dist(lca, p)+ dist(lca, q)
        
