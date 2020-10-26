"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
       
        dummy= TreeNode(0)
        dummy.right= root
        stack= [dummy]
        
        
        for _ in range(k):
            node= stack.pop()
            if node.right:
                node= node.right
                while node:
                    stack.append(node)
                    node= node.left
            
            
        
        return stack[-1].val

#---Method 2: recursion

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        self.count= 0
	self.res= None
        self.helper(root, k)
        
        return self.res
    
    def helper(self, root, k):
        if not root:
            return
      
	self.helper(root.left, k)
        self.count += 1
        if self.count == k:
            self.res = root.val
            return
        self.helper(root.right, k)
