# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def expTree(self, s: str) -> 'Node':
        
        nums = self.convert(s)
        def helper():
            val = nums.pop()
            if val.isdigit():
                root = Node(val)
                return root
            root = Node(val)
            root.right = helper()
            root.left = helper()
            return root
        return helper()
    
    def convert(self, s):
        nums, ops = [], []
        order = {"*" : 2, "/" : 2, "+" : 1, "-" : 1, "(" : 0}
        for ch in s:   
            if ch.isdigit():
                nums.append(ch)
            elif ch == "(":
                ops.append(ch)
            elif ch == ")":
                while ops and ops[-1] != "(":
                    nums.append(ops.pop())
                ops.pop()
            else:
                while ops and order[ops[-1]] >= order[ch]:
                    nums.append(ops.pop())
                ops.append(ch)
           
        while ops:
            nums.append(ops.pop())
        return nums
        
