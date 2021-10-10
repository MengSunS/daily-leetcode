class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mp = collections.defaultdict(int)
        for cd in cpdomains:
            c, d = cd.split()
            l = d.split('.')
            for i in range(len(l)):
                mp['.'.join(l[i:])] += int(c)
        return [str(v) + ' ' + k for k, v in mp.items()]
        
        
