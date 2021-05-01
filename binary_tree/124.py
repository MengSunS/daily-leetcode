# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxi = float('-inf')
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            
            self.maxi = max(self.maxi, left + right + root.val)
            return max(max(left, right) + root.val, 0) #向上返回的永远大于等于0，在leaf点开始压制的            
        helper(root)
        return self.maxi
            
    
                
        
