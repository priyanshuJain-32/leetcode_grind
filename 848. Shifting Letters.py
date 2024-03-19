class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        ret = ""
        n = len(shifts)
        prefix = [0]*(n+1)
        for i in range(n,0,-1):
            prefix[i-1] = prefix[i]+shifts[i-1]
            
        def shift(c,step):
            a = ord(c)+step%26
            if a>122:
                a-=26
            return chr(a)
        for i in range(n):
            ret += shift(s[i],prefix[i])
        return ret