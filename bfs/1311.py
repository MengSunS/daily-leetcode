
# discussion 区做法，因为指定levels,那么指定了batch循环次数

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        bfs, seen = {id}, {id}
        for _ in range(level):
            bfs = {j for i in bfs for j in friends[i] if j not in seen}
            seen |= bfs
        
        videos = Counter([v for j in bfs for v in watchedVideos[j]])
        return sorted(videos.keys(), key = lambda x: (videos[x], x))
        





















# previous 
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        q= deque([id])
        step= 0
        level_videos= defaultdict(int) 
        visited= set()
        visited.add(id)
        while q:
            for _ in range(len(q)):
                if step== level:
                    while q:
                        cur= q.popleft()
                        for video in watchedVideos[cur]:
                            level_videos[video]+= 1
                    return [k for k, v in sorted(level_videos.items(), key=lambda x: (x[1], x[0]))]
                cur= q.popleft()        
                for next in friends[cur]:
                    if next in visited: continue
                    visited.add(next)
                    q.append(next)
            step+= 1
                    
            
                
                    
                        
                        
            
        
