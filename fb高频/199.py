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
            
            
            
        
