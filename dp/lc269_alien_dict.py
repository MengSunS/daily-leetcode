from heapq import heapify, heappop, heappush

class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Write your code here
        if not words: return ""
        
        graph, in_degree= self.build_graph(words)
        if not graph: return ""
        
        return self.helper(graph, in_degree)
    
    def helper(self, graph, in_degree):
        heap= [node for node in graph if in_degree[node]==0]
        heapify(heap)
        res= ''
        
        while heap:
            node= heappop(heap)
            res+= node
            
            for nxt in graph[node]:
                in_degree[nxt]-= 1
                if in_degree[nxt]==0:
                    heappush(heap, nxt)
        return res if len(res)== len(graph) else ""
    
    def build_graph(self, words):
        graph, in_degree= {}, {}
        
        for w in words:
            for i in range(len(w)):
                graph[w[i]]= []
                in_degree[w[i]]= 0
        
        for i in range(len(words)-1):
            w1, w2= words[i], words[i+1]
            p= 0
            min_len= min(len(w1), len(w2))
            
            
            while p< min_len and w1[p]== w2[p]:
                p+= 1
            
            if p< min_len:
                graph[w1[p]].append(w2[p])
                in_degree[w2[p]]+= 1
                
            if p== min_len and len(w1)> len(w2):
                return None, None
        
        return graph, in_degree
