class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        groupIdNext= m
        for i in range(n):
            if group[i]== -1:
                group[i]= groupIdNext
                groupIdNext+= 1
        graph= collections.defaultdict(list)
        for i in range(n):
            graph[group[i]].append(i)
            
        inGroupGraph= collections.defaultdict(list)
        inGroupIndegree= collections.defaultdict(int)
        for i in range(n):
            for j in beforeItems[i]:
                if group[i]!= group[j]:
                    continue
                inGroupGraph[j].append(i)
                inGroupIndegree[i]+= 1
                
        graphGroupOrdered= collections.defaultdict(list)
        
        for groupID, groupItems in graph.items():
            
            res= self.toposort(groupItems, inGroupGraph, inGroupIndegree)
            if len(res)!= len(groupItems):
                return []
            graphGroupOrdered[groupID]= res
        
        graphGroupId= collections.defaultdict(list)
        graphGroupIdIndegree= collections.defaultdict(int)
        for i in range(n):
            for j in beforeItems[i]:
                if group[i]== group[j]:
                    continue
                if i not in graphGroupId[j]:
                    graphGroupId[group[j]].append(group[i])
                    graphGroupIdIndegree[group[i]]+= 1
        groupIds= [i for i in range(groupIdNext)]
        groupIdsOrdered= self.toposort(groupIds, graphGroupId, graphGroupIdIndegree)
        if len(groupIdsOrdered)!= len(groupIds):
            return []
        res= []
        for groupID in groupIdsOrdered:
            for node in graphGroupOrdered[groupID]:
                res.append(node)
        return res
            
        
        
        
        
    
        
        
    def toposort(self, nodes, graph, in_degree):
        start_nodes= [node for node in nodes if in_degree[node]==0]
        q= collections.deque(start_nodes)
        res= []
        while q:
            node= q.popleft()
            res.append(node)
            for nxt in graph[node]:
                in_degree[nxt]-= 1
                if in_degree[nxt]==0:
                    q.append(nxt)
        return res
    
    
            
            
            
                
        
                
        
