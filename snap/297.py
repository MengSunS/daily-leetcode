class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def encode(node):
            if not node:
                res.append('#')
                return 
            else:
                res.append(str(node.val))
            encode(node.left)
            encode(node.right)
        encode(root)
        return ' '.join(res)
            
    
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = iter(data.split())
        def decode():
            val = next(data)
            if val == '#':
                return None
            node = TreeNode(val)
            node.left = decode()
            node.right = decode()
            return node
        return decode()

