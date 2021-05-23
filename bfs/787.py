# 跟模板Dijkstra不同的地方是：加了额外一个限制，需要段数小于一个数。标准模板是设置一个set里面记好每个点是否访问过，访问过则之前的肯定比现在又访问时小，那么现在又访问时直接discard.当加了stops limit时，尽管一个点之前更快（更便宜）访问过，段数可能比第二次访问时大，导致通过此点通往目标点总段数超过。所以seen里面可以记录访问每个点时需要的段数，若第二次遇到该店的段数比之前小，是可以重新替换seen记录，并在此基础上（time & stops）进行拓展的。也可以不加seen,不管第二次遇到同一个点时段数比之前还要大，也会被进行拓展，超时。

class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        K += 1
        graph = collections.defaultdict(list)
        for s, d, p in flights:
            graph[s].append((d, p))
        pq = [(0, 0, src)]
        seen = {}
        while pq:
            cost, stops, cur = heapq.heappop(pq)
            if cur == dst and stops <= K:
                return cost
            if stops < K:
                if cur not in seen or seen[cur] > stops:
                    seen[cur] = stops
                    for nxt, dc in graph[cur]:
                        heapq.heappush(pq, (cost + dc, stops + 1, nxt))
        return -1






class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        cities= defaultdict(list)
        for u, v, w in flights:
            cities[u].append((v, w))
        
        hp= [(0, -1, src)]
        while hp:
            price, stops, city= heapq.heappop(hp)
            #第一个相等时就是最小的cost,不可能有多绕几个比目前的更小的情况，因为当前的都比这个大，多加几个站的价格是正的，只能越加越大
            if city== dst and stops<= K:
                return price
            elif stops< K:    
                for nxt, delta_p in cities[city]:
                    heapq.heappush(hp, (price+ delta_p, stops+1, nxt))
        return -1
                
            
        
