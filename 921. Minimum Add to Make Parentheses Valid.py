class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        ans = 0
        for c in s:
            if c=="(":
                stack.append(c)
            elif c==")":
                if stack:
                    stack.pop()
                else:
                    ans += 1
        return ans + len(stack)