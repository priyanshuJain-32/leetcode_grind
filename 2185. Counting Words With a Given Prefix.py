class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        def match(s,p):
            i = len(p)-1
            if i+1>len(s):
                return 0
            while i>-1:
                if s[i]!=p[i]:
                    return 0
                i-=1
            return 1
        ans = 0
        for w in words:
            ans += match(w,pref)
        return ans