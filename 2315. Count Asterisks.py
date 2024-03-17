class Solution:
    def countAsterisks(self, s: str) -> int:
        s = s.split("|")
        ans = 0
        for i in range(0,len(s),2):
            ans += s[i].count("*")
        return ans