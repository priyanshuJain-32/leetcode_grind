class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        if n<3:
            return 0
        i, j, cnt = 0, 3, 0
        sub = deque(s[i:j])
        while j<=n:
            if len(set(s[i:j]))==3:
                cnt += 1
            i, j = i+1, j+1
        return cnt