class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for c in details:
            if int(c[11:13])>60:
                ans += 1
        return ans