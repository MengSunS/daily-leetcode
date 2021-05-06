# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
       
        def get_left(root):
            if not root or not (root.left or root.right):
                return 
            
            boundary.append(root.val)
            if root.left: 
                get_left(root.left)
            elif root.right:
                get_left(root.right)
                
                
        def get_right(root):
            if not root or not (root.left or root.right):
                return 
 
            if root.right: 
                get_right(root.right)
            elif root.left:
                get_right(root.left)
            boundary.append(root.val)
                    
       
        def get_bottom(node):
            if not node:
                return 
            if node != root and not node.left and not node.right:
                boundary.append(node.val)
                return 
            get_bottom(node.left)
            get_bottom(node.right)
        
        boundary = [root.val]
        get_left(root.left)
        get_bottom(root)
        get_right(root.right)
        
        return boundary
        
