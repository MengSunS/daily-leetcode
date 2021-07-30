class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: x[1] - x[0])
        res = 0
        n = len(costs) // 2
        for i in range(n):
            res += costs[i][1] + costs[i + n][0]
        return res
            
       

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        firstCity = [i for i, j in costs]
        diff = [j - i for i, j in costs]
        return sum(firstCity) + sum(sorted(diff)[:len(costs)//2]) 
