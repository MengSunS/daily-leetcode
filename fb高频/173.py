# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.go_left(root)
    
    def go_left(self, root):
        self.stack.append(root)
        while root.left:
            root = root.left
            self.stack.append(root)
        

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self.go_left(node.right)
        return node.val
        

    def hasNext(self) -> bool:
        return len(self.stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
