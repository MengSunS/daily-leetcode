# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(l, r):
            if l > r: return
            val = postorder[self.p]
            root = TreeNode(val)
            self.p -= 1
            idx = inorder_map[val]
            root.right = build(idx+1, r) #下一个postorder是右边subtree的root,要把它给到inorder中l, root, r 中right的那个subtree，可以错着试一下
            root.left = build(l, idx-1)
            return root
        self.p = len(postorder) - 1
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        return build(0, len(inorder)-1)
        
        
        
