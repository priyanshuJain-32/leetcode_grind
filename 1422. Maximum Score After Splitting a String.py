class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        prefix_0 = [0]*(n+1)
        suffix_1 = [0]*(n+1)
        for i in range(n):
            if s[i]=="0":
                prefix_0[i+1] = prefix_0[i]+1
            elif s[i]=="1":
                prefix_0[i+1] = prefix_0[i]
            if s[n-i-1]=="1":
                suffix_1[n-i-1] = suffix_1[n-i] + 1
            elif s[n-i-1]=="0":
                suffix_1[n-i-1] = suffix_1[n-i]
        ans = 0
        for i,j in zip(prefix_0[1:-1], suffix_1[1:-1]):
            ans = max(i+j, ans)
        return ans