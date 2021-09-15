class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.isWord = True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.res = []
        m, n = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)
        node = trie.root
        for i in range(m):
            for j in range(n):
                self.dfs(i, j, board, node, m, n, '')
        return self.res

    def dfs(self, i, j, board, node, m, n, path):
        if node.isWord:
            self.res.append(path)
            node.isWord = False
            # return #这里不能加return,dfs找路径前半段在trie里，append进去得继续这个这个路径往下找。 
        
        if i >= m or i < 0 or j >= n or j < 0:
            return 
        if board[i][j] not in node.children:
            return 
        node = node.children[board[i][j]]
        tmp = board[i][j]
        board[i][j] = '#'
        for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            self.dfs(ni, nj, board, node, m, n, path + tmp)
        board[i][j] = tmp
    
    
            
            
            
        
