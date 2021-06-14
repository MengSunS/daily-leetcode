# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder: return None
        
        pos= inorder.index(postorder[-1])
        root= TreeNode(postorder[-1])
        
        root.left= self.buildTree(inorder[:pos], postorder[:pos])
        root.right= self.buildTree(inorder[pos+1:], postorder[pos:-1])
        return root
        
