# iterative 

# time O(N), each node at most process twice, space is O(1)
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        node = root
        while node:
            if node.left:
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right
                rightmost.right = node.right
                node.right = node.left
                node.left = None
            node = node.right

# recursion

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flattenTree(node):
            if not node:
                return None
            
            if not node.left and not node.right:
                return node
    
            l_t = flattenTree(node.left)
            r_t = flattenTree(node.right)
            
            if l_t:
                l_t.right = node.right
                node.right = node.left
                node.left = None
                
            return r_t if r_t else l_t #主要错的是helper函数没返回，每个当前 的node需要返回tail node. 只要调用递归有返回，上级递归函数主体必然要返回。这应该归咎于cs基础缺失。
        
        flattenTree(root)
