# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0, float('inf'), float('-inf')
            l_n, l_min, l_max = dfs(node.left)
            r_n, r_min, r_max = dfs(node.right)
            if l_max < node.val < r_min:
                return l_n + r_n + 1, min(node.val, l_min), max(node.val, r_max)
            else:
                return max(l_n, r_n), float('-inf'), float('inf')
        return dfs(root)[0]
        
