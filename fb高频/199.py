# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        q, nq, res = [], [], []
        if root: 
            q.append(root)
      
        while q:
            res.append(q[-1].val)
            for node in q:
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            q, nq = nq, []
        return res
            
            
            
# dfs almost preorder,right first then left, dict only records first time encounters this level H. Inorder, posorder travseve 都可以，不过顺序是从底网上
time O(N), space O(h), O(N) is till travser all points. 


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = {}
        def dfs(root, h):
            if not root:
                return 
            if h not in ans:
                ans[h] = root.val
            dfs(root.right, h + 1)
            dfs(root.left, h + 1)
            
        dfs(root, 0)
        return [ans[i] for i in ans.keys()]        
