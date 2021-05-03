


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


# Or, change the tree node structure if allowed.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.parent = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def build_graph(node, parent):
            if not node: return 
            node.parent = parent 
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
                for nei in [node.left, node.right, node.parent]:
                    if not nei:
                        continue
                    if nei in seen:
                        continue
                    seen.add(nei)
                    q.append((nei, dist + 1))
        
        return res

        
                
# Or, dfs + dfs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.parent = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def build_graph(node, parent):
            if not node: return 
            dict[node] = parent 
            build_graph(node.left, node)
            build_graph(node.right, node)
        
        dict = {}
        build_graph(root, None)
        print(dict)
        q = deque([(target, 0)])
        seen = set()
        
        
        def dfs(node, distance):
            if node is None or node in visited:
                return
            visited.add(node)
            
            if distance == K:
                ans.append(node.val)
            elif distance < K:
                dfs(node.left, distance+1)
                dfs(node.right, distance+1)
                dfs(parentMap[node], distance+1)
        
        ans = []
        visited = set()
        parentMap = dict
        dfs(target, 0)
        
        return ans
      

        
                
                
        
