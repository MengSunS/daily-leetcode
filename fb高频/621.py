class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = list(collections.Counter(tasks).values())
        f_max = max(c)
        n_max = c.count(f_max)
        return max(len(tasks), (f_max - 1) * (n + 1) + n_max)



class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = collections.Counter(tasks)
        pq = []
        for f in c.values():
            heapq.heappush(pq, (-f))
        f_max = -heapq.heappop(pq)
        slots = (f_max - 1) * n
        while pq:
            cur_f= -heapq.heappop(pq)
            slots -= min(f_max - 1, cur_f)
        return len(tasks) + max(slots, 0)
        
