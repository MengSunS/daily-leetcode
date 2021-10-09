class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.word = None
        
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(i, j, node):
            if node.word:
                res.append(node.word)
                node.word = None
                
            if not m > i >= 0 <= j < n:
                return False
            if board[i][j] not in node.children:
                return False
            node = node.children[board[i][j]]
            
            tmp = board[i][j]
            board[i][j] = '#'
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                dfs(ni, nj, node)
            board[i][j] = tmp
        
  
        
        m, n = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)
            
        res = []
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie.root)
        return res
        
