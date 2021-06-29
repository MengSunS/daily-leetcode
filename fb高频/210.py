class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        nxt_courses = collections.defaultdict(list)
        in_degree = {i: 0 for i in range(numCourses)}
        for a, b in prerequisites:
            in_degree[a] += 1
            nxt_courses[b].append(a)
        q = collections.deque([course for course in in_degree if in_degree[course] == 0])
        res = []
        while q:
            cur = q.popleft()
            res.append(cur)
            for nxt in nxt_courses[cur]:
                in_degree[nxt] -= 1
                if not in_degree[nxt]:
                    q.append(nxt)
        return res if len(res) == numCourses else []
            
            
        
