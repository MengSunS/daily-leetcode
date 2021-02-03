class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet= set(wordList)
        if endWord not in wordSet: return []
        layer= defaultdict(list)
        layer[beginWord]= [[beginWord]]
        
        while layer:
            nextLayer= defaultdict(list)
            for word in layer:
                if word== endWord:
                    return layer[word]
                for i in range(len(word)):
                    for char in string.ascii_lowercase:
                        newWord= word[:i]+ char+ word[i+1:]
                        if newWord in wordSet:  #这里不需要全局visited去重，同一层的不同单词可以在下一层到达同一个单词
                            nextLayer[newWord]+= [path+ [newWord] for path in layer[word]]
            wordSet-= set(nextLayer.keys())
            layer= nextLayer
        return []
