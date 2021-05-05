#两个stack的方法比一个stack节省时间，一个stack need [q.popleft for _ in range(len(q))]需要额外O(n)清空，两个stack的话直接switch

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        q = deque([(root, 1)])
        res = []
        
        while q:
            res.append(list(node.val for node, _ in q)[::q[0][1]])
            stack = []
            for node, flag in q:
                if node.left: stack.append((node.left, -flag))
                if node.right: stack.append((node.right, -flag))
            q = stack
                   
        return res
