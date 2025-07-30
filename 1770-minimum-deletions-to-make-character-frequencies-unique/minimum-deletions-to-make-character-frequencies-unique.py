class Solution:
    def minDeletions(self, s: str) -> int:
        mapfreq = {}
        res = 0
        used = set()
        for c in s:
            mapfreq[c] = mapfreq.get(c,0)+1
        
        for v,f in mapfreq.items():
            while f > 0 and f in used:
                f -= 1
                res += 1
            used.add(f)
        return res
        
            
        