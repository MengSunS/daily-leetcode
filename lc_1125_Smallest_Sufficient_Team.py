class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        
        dp= {0: []}
        req_skills= {skill: idx for idx, skill in enumerate(req_skills)}
        n= len(req_skills)
        N= 1<<n
        
        for idx, person in enumerate(people):
            
            person_val= 0
            for skill in person:
                if skill not in req_skills:
                    continue
                person_val+= 1<< (req_skills[skill])
                      
            for status, team in list(dp.items()):
                nextStatus= status | person_val
                if nextStatus== status:
                    continue
                             
                if nextStatus not in dp or len(dp[nextStatus])> len(dp[status])+ 1:
                    dp[nextStatus]= team+ [idx]
        
        return dp[N-1]

                
            
            
                
        
        
