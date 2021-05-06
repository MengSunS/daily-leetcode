# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, r: TreeNode, s: TreeNode) -> bool:
        if not r: return False
        if r.val == s.val and self.check(r, s):
            return True
        return self.isSubtree(r.left, s) or self.isSubtree(r.right, s)
    def check(self, r, s):
            if not r and not s:
                return True
            if (not r and s) or (r and not s):
                return False
            
            if r.val != s.val:
                return False
            return self.check(r.left, s.left) and self.check(r.right, s.right)
        

        
        
            
        
