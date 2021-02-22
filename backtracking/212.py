class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def btr(path, i, j, visited, target):
            if path== target:
                return True
            if len(path)> len(target):
                return
                
            for di, dj in directions:
                ni, nj= i+ di, j+ dj
                if ni>= m or ni< 0 or nj>= n or nj< 0: 
                    continue
                if (ni, nj) in visited:
                    continue
                visited.add((ni, nj))
                if btr(path+board[ni][nj], ni, nj, visited, target):
                       return True
                visited.remove((ni, nj))
        
            return False
                
                
        res= []
        directions= [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n= len(board), len(board[0])
        words= set(words)
        for word in words:
            for i in range(m):
                for j in range(n):
                    visited= set()
                    if board[i][j]== word[0] and btr('', i, j, set([(i, j)]), word[1:]):  
                        res.append(word)
                        break
                else:
                    continue
                break
                             
        return res

                
        
