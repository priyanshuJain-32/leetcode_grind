class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        def hcf(a,b):
            if a%b==0:
                return b
            return hcf(b,a%b)
        
        d = max(a,b)
        e = min(a,b)
        h = hcf(d,e)
        f = {h}
        for i in range(h//2+1,0,-1):
            f.add(hcf(h,i))
        return len(f)