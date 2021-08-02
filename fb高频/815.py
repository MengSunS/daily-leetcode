class Solution:
    def numBusesToDestination(self, routes, source, target):
        stop2bus = collections.defaultdict(list)
        for bus, stops in enumerate(routes):
            for stop in stops:
                stop2bus[stop].append(bus)
        seen_stop = set([source])
        q = [(source, 0)]
        
        for stop, step in q:
            if stop == target: 
                return step
            for bus in stop2bus[stop]:
                for nxtStop in routes[bus]:
                    if nxtStop not in seen_stop:
                        seen_stop.add(nxtStop)
                        q.append((nxtStop, step + 1))
                routes[bus] = []
                   
        return -1
        
       
                    
        
# same

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        stop2bus = collections.defaultdict(list)
        for bus, stops in enumerate(routes):
            for stop in stops:
                stop2bus[stop].append(bus)
        seen_bus, seen_stop = set(), set([source])
        q = collections.deque([(source, 0)])
        while q:
            stop, step = q.popleft()
            if stop == target: return step
            for nxtBus in stop2bus[stop]:
                if nxtBus in seen_bus:
                    continue
                seen_bus.add(nxtBus)
                for nxtStop in routes[nxtBus]:
                    if nxtStop in seen_stop:
                        continue
                    seen_stop.add(nxtStop)
                    q.append((nxtStop, step + 1))
                  
        return -1
                     
