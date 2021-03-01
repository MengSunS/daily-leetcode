class TrieNode:
    def __init__(self):
        self.children= defaultdict(TrieNode)
        self.is_word= False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root= TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur= self.root
        for w in word:
            cur= cur.children[w]
        cur.is_word= True
            
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur= self.root
        for w in word:
            if w not in cur.children:
                return False
            cur= cur.children[w]
            
        return cur.is_word
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur= self.root
        for w in prefix:
            if w not in cur.children:
                return False
            cur= cur.children[w]
            
        return True
