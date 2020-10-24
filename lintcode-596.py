"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        if not root: return None
        self.min_sum= sys.maxsize
        self.node= None
        self.helper(root)
        return self.node
        
    
    def helper(self, root):
        if not root:
            return 0
        
        cur= self.helper(root.left)+ self.helper(root.right)+ root.val
        
        if cur< self.min_sum:
            self.min_sum= cur
            self.node= root
        
        return cur

