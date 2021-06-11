class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        hp = [(nums1[0] + nums2[0], 0, 0)]
        seen = set((0, 0))
        res = []
        while len(res) < k and hp:
            s, idx1, idx2 = heapq.heappop(hp)
            res.append((nums1[idx1], nums2[idx2]))
            seen.add((idx1, idx2))
            if idx1 + 1 < len(nums1) and (idx1 + 1, idx2) not in seen:
                seen.add((idx1 + 1, idx2))
                heapq.heappush(hp, (nums1[idx1 + 1] + nums2[idx2], idx1 + 1, idx2))
            if idx2 + 1 < len(nums2) and (idx1, idx2 + 1) not in seen:
                seen.add((idx1, idx2 + 1))
                heapq.heappush(hp, (nums1[idx1] + nums2[idx2 + 1], idx1, idx2 + 1))
        return res
        
