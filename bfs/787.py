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
                
            
        
