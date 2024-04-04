class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        i, j, ans, n = 0, 0, 0, len(s)
        d = collections.defaultdict(int)
        while j<n:
            d[s[j]]+=1
            while d[s[j]]>2:
                d[s[i]]-=1
                i+=1
            ans = max(ans,j-i+1)
            j+=1
        return ans