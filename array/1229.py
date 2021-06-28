class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        i, j = 0, 0
        m, n = len(slots1), len(slots2)
        while i < m and j < n:
            s, e = max(slots1[i][0], slots2[j][0]), min(slots1[i][1], slots2[j][1])
            if s <= e and e - s >= duration:
                return [s, s + duration]

            if slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1
        return []
                
        
