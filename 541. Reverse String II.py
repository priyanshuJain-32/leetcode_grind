class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        d = -1
        ans = ""
        for i in range(0,len(s),k):
            ans += s[i:i+k][::d]
            d *= -1
        return ans