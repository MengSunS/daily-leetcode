# translation: longest subarray with atMost 2 distinct integers
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        res = i = 0
        n = len(tree)
        count = {}
        for j in range(n):
            count[tree[j]] = count.get(tree[j], 0) + 1
            while len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
            res = max(res, j - i + 1)
        return res
                
            
# translation: longest subarray with atMost 2 distinct integers
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        res = i = 0
        n = len(tree)
        count = {}
        for j in range(n):
            count[tree[j]] = count.get(tree[j], 0) + 1
            if len(count) > 2:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
        return j - i + 1
                
            
                
