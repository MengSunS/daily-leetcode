class Solution:
    def isSubtree(self, r: TreeNode, s: TreeNode) -> bool:
        if not r:
            return 
        if r.val == s.val and self.match(r, s):
            return True
        return self.isSubtree(r.left, s) or self.isSubtree(r.right, s)
    
    def match(self, r, s):
        if r and s:
            return r.val == s.val and self.match(r.left, s.left) and self.match(r.right, s.right)
        return r == s
