class Solution:
    def maxDepth(self, s: str) -> int:
        stack = 0
        m = 0
        for p in s:
            if p=="(":
                stack += 1
                m = max(m, stack)
            elif p==")":
                stack-=1
        return m
