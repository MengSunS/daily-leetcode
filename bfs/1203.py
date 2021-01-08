# graph: {groupdID: [group members]}, group members排序， groupIDs排序，排序用另外两个对应的graph实现，graph1: {item: [nxt items]}, graph2: {groupId: [nxt groupIds]}.两个graph1 & graph2分别通过组内，group[i]!= group[j], j为beforeItems[i]对应的list循环；以及group[i]== group[j]代表不同组时，graph2[group[j]].append(group[i])来实现。




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
    
    
            
            
            
                
        
                
        
