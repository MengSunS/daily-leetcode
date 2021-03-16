class Solution:
    def removeInterval(self, A: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        del_s, del_e = toBeRemoved
        res = []
        for start, end in A:
            if start >= del_e or end <= del_s:
                res.append([start, end])
            else:
                if start < del_s:
                    res.append([start, del_s])
                if end > del_e:
                    res.append([del_e, end])
        return res
        
        
