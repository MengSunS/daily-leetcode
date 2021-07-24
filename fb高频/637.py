# Method 1: bfs

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        q, nq = [root], []
        res = [root.val]
        while q:
            for node in q:
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            q, nq, tmp = nq, [], []
            if q:
                for node in q:
                    tmp.append(node.val)
                res.append(sum(tmp) / len(tmp))
        return res


# Method 2: dfs

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        info = []
        def dfs(node, depth):
            if not node:
                return 
            if len(info) <= depth:
                info.append([0, 0])
            info[depth][0] += node.val
            info[depth][1] += 1
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 0)
        return [s/c for s, c in info]
