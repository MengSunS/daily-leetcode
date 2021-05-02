# Method 1: define value range for subtree

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, left, right):
            if not root:
                return True
            return left < root.val < right and helper(root.left, left, root.val) and helper(root.right, root.val, right)
        
        left, right = float('-inf'), float('inf')
        return helper(root, left, right)

# Method 2: in_order and record prev

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder(root):
            nonlocal prev
            if not root:
                return True
            
            if not inorder(root.left):
                return False
            if prev and root.val <= prev.val:
                return False
            prev = root
            return inorder(root.right)
        
        prev = None
        return inorder(root)
