class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        queries_sort= sorted(enumerate(queries), key=lambda x: x[1][1])
        res= [-1]*len(queries)
        trie= Trie()
        j= 0
        for idx, (x, m) in queries_sort:
            while j< len(nums) and nums[j]<= m:
                trie.insert(nums[j])
                j+= 1
            res[idx]= trie.query(x)
        return res
    
class Trie:
    def __init__(self):
        self.root= {}
    
    def insert(self, num):
        node= self.root
        for i in range(31, -1, -1):
            bit= (num>>i) & 1
            if bit not in node:
                node[bit]= {}
            node= node[bit]
    
    def query(self, num):
        if not self.root: return -1
        node= self.root
        res= 0
        for i in range(31, -1, -1):
            bit= (num>>i) & 1
            if 1-bit in node:
                node= node[1-bit]
                res |= (1<<i)
            else:
                node= node[bit]
        return res
    
