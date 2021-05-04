# method 1: take advantage of complete tree, O(logN ^ 2)

# time: O(logN ^ 2). 每层2**(d - 1), 前d层总数2**d-1 
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        lh, rh = self.getH(root.left), self.getH(root.right)
        if lh == rh: #左子树一定满, 2**lh-1为左子树上的个数，+1为root
            return pow(2, lh) - 1 + 1 + self.countNodes(root.right)
        else: #右子树一定满
            return pow(2, rh) - 1 + 1 + self.countNodes(root.left)
    
    def getH(self, node):  
        ret = 0
        while node:
            ret += 1
            node = node.left
        return ret

# method 2: worse performace, linear time



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.left and not root.right:
            return 1
        left = self.countNodes(root.left)
        right = self.countNodes(root.right)
        return left + right + 1
