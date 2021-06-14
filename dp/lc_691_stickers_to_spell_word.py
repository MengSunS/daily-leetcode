class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        n= len(target)
        N= 1<<n
        dp= [sys.maxsize]*N
        dp[0]= 0
        
        for i in range(N):
            if dp[i]==sys.maxsize:
                    continue
            for sticker in stickers:
                j= self.findNextStatus(i, sticker, target)
                if j==i: continue # if last sticker was useless and made no difference
                dp[j]= min(dp[j], dp[i]+1) # dp[i] is same within the same loop through stickers, so if next status jumps to the sme status, take the minimum stickers cost
                
        return dp[-1] if dp[-1]!= sys.maxsize else -1
    
    def findNextStatus(self, status, sticker, target):
        for ch in sticker:
            for i in range(len(target)):
                if ((status>>i)&1)== 0 and target[i]== ch:
                    status+= 1<<i
                    break # if find ch can get into status, break the inner loop so that the same ch will not use twice, then continue next ch in the same sticker, so guaranteed utilized the same sticker at most
        return status
                    
        
