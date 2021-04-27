# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def dfs(root, path, target):
            if root:
                if not root.left and not root.right and target == root.val:
                    res.append(path + [root.val])
                    return 
                dfs(root.left, path + [root.val], target - root.val)
                dfs(root.right, path + [root.val], target - root.val)
            
        res = []
        dfs(root, [], targetSum)
        return res
