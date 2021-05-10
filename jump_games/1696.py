class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        scores = [0] * n
        scores[0] = nums[0]
        dq = deque([0])
        for i in range(1, n):
            if dq[0] == i - k -1:
                dq.popleft()
            scores[i] = scores[dq[0]] + nums[i]
            while dq and scores[dq[-1]] <= scores[i]: # while dq cuz when scores[i] is the maximum
                dq.pop()
            dq.append(i)
        return scores[-1]
        
