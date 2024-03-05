class Solution:
    def minimumLength(self, s: str) -> int:
        i = 0
        j = len(s)-1
        cur = s[0]
        while i<j:
            if s[j]!=cur:
                return j-i+1
            while s[i]==cur and i<j:
                i+=1
            while s[j]==cur and j>i:
                j-=1
            if i==j:
                if len(set(s))==1:
                    return 0
            s = s[i:j+1]
            j -= i
            i = 0
            cur = s[0]
        return len(s)