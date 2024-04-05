class Solution:
    def makeGood(self, s: str) -> str:
        def clean(s):
            ans = ""
            s+="{"
            i = 0
            while i<len(s)-1:
                if abs(ord(s[i])-ord(s[i+1]))==32:
                    i+=2
                else:
                    ans+=s[i]
                    i+=1
            return ans
        t = clean(s)
        while s!=t:
            s = t
            t = clean(s)
        return t