class Solution:
    def palindromePairs(self, words):

        def all_valid_prefixes(word):
            valid_prefix= [word]
            for i in range(len(word)):
                if word[i:]== word[i:][::-1]:
                    valid_prefix.append(word[:i])
            return valid_prefix
                
            
        def all_valid_suffixes(word):
            valid_suffix= []
            for i in range(len(word)):
                if word[:i+1]== word[:i+1][::-1]:
                    valid_suffix.append(word[i+1:])
            return valid_suffix
                
        res= []
        wordDict= {word: i for i, word in enumerate(words)}

        for idx, word in enumerate(words):
            # if word[::-1] in wordDict and wordDict[word[::-1]]!= wordDict[word]:
            #     res.append(idx)
            for val_pre in all_valid_prefixes(word):
                if val_pre[::-1] in wordDict and wordDict[val_pre[::-1]]!= idx:
                    res.append([idx, wordDict[val_pre[::-1]]])
            
            for val_suf in all_valid_suffixes(word):
                if val_suf[::-1] in wordDict and wordDict[val_suf[::-1]]!= idx:
                    res.append([wordDict[val_suf[::-1]], idx])
        return res
