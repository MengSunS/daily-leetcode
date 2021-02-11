# Method 1: bfs


"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        map= {}
        for e in employees:
            map[e.id]= e
        q= deque([id])
        res= 0
        while q:
            cur= q.popleft()
            res+= map[cur].importance
            for next in map[cur].subordinates:
                q.append(next)
        return res
            
        

# Method 2: dfs recursion

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        table = {}
        for employee in employees:
            table[employee.id] = employee
        return self.helper(table, id)

    def helper(self, table, rootId):
        root = table[rootId]
        total = root.importance
        for subordinate in root.subordinates:
            total += self.helper(table, subordinate)
        return total
