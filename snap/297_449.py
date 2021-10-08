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
            
    
        
# BST lc 449

class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        def encode(node):
            if not node:
                return 
            res.append(str(node.val))
            encode(node.left)
            encode(node.right)
        encode(root)
        return ' '.join(res)
            
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        data = deque(data.split())
        def decode(lo, hi):
            if data and lo < int(data[0]) < hi:
                node = TreeNode(int(data.popleft()))
                node.left = decode(lo, node.val)
                node.right = decode(node.val, hi)
                return node
            else:
                return None
        return decode(float('-inf'), float('inf'))
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

