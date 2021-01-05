class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        graph, in_degree= self.build_graph(seqs)
        #如果有带环的不会进入q但结果会res==org
        if len(graph)!= len(org): return False
        start_nodes= [node for node in in_degree if in_degree[node]==0]
        res= []
        q= collections.deque(start_nodes)
        
        while q:
            #anytime, 防止num of start_nodes就>1
            if len(q)> 1:
                return False
            node= q.popleft()
            res.append(node)
            for nxt in graph[node]:
                in_degree[nxt]-= 1
                if in_degree[nxt]== 0:
                    q.append(nxt)
               
        return res== org 
                    
               
    
    def build_graph(self, ss):
        in_degree= {}
        graph= {}
        for s in ss:
            for c in s:
                graph[c]= []
                in_degree[c]= 0
                
        for s in ss:
            for i in range(len(s)-1):
                graph[s[i]].append(s[i+1])
                in_degree[s[i+1]]+= 1
        return graph, in_degree
                
    
            
            
        
        
        
