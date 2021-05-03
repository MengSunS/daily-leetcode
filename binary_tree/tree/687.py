# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 可能的解包括三种情况： 1).包含根；2).不包含根，答案绕过一个子根；3).不包含根，答案包含一个子根但不绕。
# 需要有一个全局变量来记录并更新第二种情况。每层网上返回的是不绕过该子根的，左边或者右边最长的一个。如果当前子根与.left不相等，返回的是0，反之若相等的话，返回的是下层返回的lp = left + 1
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        
        def helper(node):
            if not node:
                return 0
            l = helper(node.left)
            r = helper(node.right)
            lp = rp = 0
            if node.left and node.val == node.left.val:
                lp = l + 1
            if node.right and node.val == node.right.val:
                rp = r + 1
            self.maxi = max(self.maxi, lp + rp)
            return max(lp, rp)
        
        self.maxi = 0
        helper(root)
        return self.maxi
            
                
