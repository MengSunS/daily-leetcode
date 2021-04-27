# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0, float('inf'), float('-inf')
            
            l_n, l_min, l_max = dfs(root.left)
            r_n, r_min, r_max = dfs(root.right)
            
            if l_max < root.val < r_min:
                return l_n + r_n + 1, min(l_min, root.val), max(r_max, root.val)
            else:
                return max(l_n, r_n), float('-inf'), float('inf')
        
        return dfs(root)[0]
            
                
    
    
    
        
