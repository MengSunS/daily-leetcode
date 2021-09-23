# each node record two values: if rob current node, maximum money can scope from all its subtrees & if not rob current node, maximum money can scope from all subtrees. 
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0, 0]
            L = dfs(node.left)
            R = dfs(node.right)
            return [node.val + L[1] + R[1], max(L) + max(R)]
        return max(dfs(root))
