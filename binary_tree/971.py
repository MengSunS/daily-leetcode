# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        def dfs(node):
            if not node: return 
            if node.val != voyage[self.index]:
                self.possible = False
                return 
            
            self.index += 1
            if node.left and node.left.val != voyage[self.index]: 
                flip.append(node.val)
                dfs(node.right)
                dfs(node.left)
            else:
                dfs(node.left)
                dfs(node.right)
        flip = [] # why this one no need self.flip?
        self.index = 0
        self.possible = True
        dfs(root)
        return flip if self.possible else [-1]
                
        
