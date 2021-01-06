class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph= collections.defaultdict(set)
        in_degree= {c: 0 for word in words for c in word}
        
        for w1, w2 in zip(words, words[1:]):
            if w1[:len(w2)]==w2 and len(w1)> len(w2):
                return ''
            max_len= min(len(w1), len(w2))
            for j in range(max_len):
                if w1[j]==w2[j]:
                    continue
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                    in_degree[w2[j]]+= 1
                break
       
        # bfs below
        
        start_char= [c for c in in_degree if in_degree[c]==0]
        q= collections.deque(start_char)
        ans= []
        while q:
            char= q.popleft()
            ans.append(char)
            for nxt in graph[char]:
                in_degree[nxt]-= 1
                if in_degree[nxt]==0:
                    q.append(nxt)
        
        return ''.join(ans) if len(ans)==len(in_degree) else ""
                
            
            
                
        
        
        
