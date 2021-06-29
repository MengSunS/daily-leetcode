class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.isWord = True
       
        

    def search(self, word: str) -> bool:
        node = self.root
        return self.dfs(node, 0, word)
    
    def dfs(self, node, i, word):
        if i == len(word):
            if node.isWord:
                return True
            return False
            
        if word[i] == '.':
            for n in node.children.values():
                if self.dfs(n, i + 1, word):
                    return True
        else:
            node = node.children.get(word[i])
            if not node:
                return False
            return self.dfs(node, i + 1, word)
                
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
