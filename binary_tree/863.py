class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def build_graph(node, parent):
            if not node: return 
            dict[node] = parent 
            build_graph(node.left, node)
            build_graph(node.right, node)
        
        dict = {}
        build_graph(root, None)
        q = deque([(target, 0)])
        seen = set([target])
        res = []
        
        while q:
            node, dist = q.popleft()
            if dist == K:
                res.append(node.val)
            elif dist < K:
                for nei in [node.left, node.right, dict[node]]:
                    if not nei:
                        continue
                    if nei in seen:
                        continue
                    seen.add(nei)
                    q.append((nei, dist + 1))
        
        return res
