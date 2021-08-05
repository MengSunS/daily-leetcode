# iterative inorder

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right

# recursion inorder, exit recursion when found 

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.res = None
        def inorder(node):
            if self.res != None:
                return 
            if not node:
                return 
            inorder(node.left)
            self.k -= 1
            if not self.k:
                self.res = node.val
            inorder(node.right)
        
        self.k = k
        inorder(root)
        return self.res
