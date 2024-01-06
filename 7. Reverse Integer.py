class Solution:
    def reverse(self, x: int) -> int:
        
        # Shorter version 2
        r = int(str(abs(x))[::-1])
        s = -1 if x<0 else 1
        return r*s if r<2147483648 else 0
        
        # Version 1
        # if x>=0:
        #     r = int(str(x)[::-1])
        #     if r>2147483647:
        #         return 0
        #     return r
        # else:
        #     r = -1*int(str(abs(x))[::-1])
        #     if r<-2147483648:
        #         return 0
        #     return r