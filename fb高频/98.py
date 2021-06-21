# method 1: in_order 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def in_order(root):
            nonlocal prev
            if not root:
                return True
            if not in_order(root.left):
                return False
            if prev != None and root.val <= prev: # 不能写not prev, cuz 当 prev值为0
                return False
            prev = root.val
            return in_order(root.right) #如果以上都能行得通，右边一锤子
        prev = None
        return in_order(root)
    

# method 2: 分左右，左右分别的上下边界，root.left时root.val为上边界，反之为下边界

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.valid(root, low=float('-inf'), high=float('inf'))
    
    def valid(self, root, low, high):
        if not root:
            return True
        if root.val >= high or root.val <= low:
            return False
        return self.valid(root.left, low, root.val) and self.valid(root.right, root.val, high)
    
