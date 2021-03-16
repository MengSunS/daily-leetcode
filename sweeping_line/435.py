# 3 cases, greedy goal is to leave more space
# Method 1

class Solution:
    def eraseOverlapIntervals(self, A: List[List[int]]) -> int:
        # sort by ending points and greedy
        A.sort(key=lambda x: x[1])
        j = 0
        cnt = 0
        for i in range(1, len(A)):
            if A[i][0] >= A[j][1]:
                j = i
            else:
                cnt += 1
        return cnt

# Method 2

class Solution:
    def eraseOverlapIntervals(self, A: List[List[int]]) -> int:
        # sort by ending points and greedy
        A.sort(key=lambda x: x[1])
        j = 0
        cnt = 0
        for i in range(1, len(A)):
            if A[i][0] >= A[j][1]:
                j = i
            else:
                cnt += 1
        return cnt
        
