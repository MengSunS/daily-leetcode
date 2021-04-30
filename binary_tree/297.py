# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        def doit(node):
            if not node:
                res.append('#')
                return
            res.append(str(node.val))
            doit(node.left)
            doit(node.right)
            
        res = []
        doit(root)
        return ' '.join(res)
            
            

    def deserialize(self, data):
        def undo():
            val = next(data) 
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = undo()
            node.right = undo()
            return node
        
        data = iter(data.split())
        return undo()
            
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
