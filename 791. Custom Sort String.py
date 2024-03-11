class Solution:
    def customSortString(self, order: str, s: str) -> str:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        alphas = {k:0 for k in alphabets}
        for i in s:
            alphas[i] += 1
        ans = ""
        for i in order:
            while alphas[i]>0:
                ans+=i
                alphas[i]-=1
                s= s.replace(i,"")
        ans += s
        return ans