"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        if not root:
            return None
        
        lca, a_exist, b_exist= self.helper(root, A, B)
        if a_exist and b_exist:
            return lca
        else:
            return None
    
    def helper(self, root, A, B):
        if not root:
            return None, 0, 0
            
        left_lca, a_exist_left, b_exist_left= self.helper(root.left, A, B)
        right_lca, a_exist_right, b_exist_right= self.helper(root.right, A, B)
        
        a_exist= a_exist_left or a_exist_right or A==root
        b_exist= b_exist_left or b_exist_right or B==root
        
        # if not (a_exist and b_exist):
        #     return None, a_exist, b_exist
        
        if root==A or root==B:
            return root, a_exist, b_exist
        
        if left_lca and right_lca:
            return root, a_exist, b_exist
        
        if left_lca:
            return left_lca, a_exist, b_exist
        if right_lca:
            return right_lca, a_exist, b_exist
        else:
            return None, a_exist,b_exist
