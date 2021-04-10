# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(l, r):
            if l > r: return 
            val = preorder[self.p]
            root = TreeNode(val)
            self.p += 1 # binary tree中没有回溯，只是recursion
            idx = inorder_map[val]
            root.left = build(l, idx-1)
            root.right = build(idx+1, r)
            return root
        
        self.p = 0
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        return build(0, len(inorder)-1)
        
        
