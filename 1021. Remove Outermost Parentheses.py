class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = 0
        ans = ""
        prev= 0
        for i in range(len(s)):
            if s[i]=="(":
                stack += 1
            else:
                stack -= 1
            if stack==0:
                ans += s[prev+1:i]
                prev = i+1
        return ans