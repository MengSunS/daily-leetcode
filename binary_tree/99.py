# Method 1: iterative


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        x = y = pre = None
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if pre and node.val < pre.val:
                y = node
                if not x:
                    x = pre
                else:
                    break
            pre = node
            node = node.right
        
        x.val, y.val= y.val, x.val


# Method 2: recursion

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def find_two_swapped(root: TreeNode):
            nonlocal x, y, pre
            if not root:
                return 
            find_two_swapped(root.left)
            if pre and root.val< pre.val:
                y= root
                if not x:
                    x= pre
                else:
                    return 
            pre= root
            find_two_swapped(root.right)
        
        x, y, pre= None, None, None
        find_two_swapped(root)
        x.val, y.val= y.val, x.val
