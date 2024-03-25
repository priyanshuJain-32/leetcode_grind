class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indices = []
        for i,v in enumerate(s):
            if v==c:
                indices.append(i)
        ans = []
        n = len(s)
        for i in range(n):
            near = n
            for ind in indices:
                v = abs(i-ind)
                if v<near:
                    near = v
                else:
                    break
            ans.append(near)
        return ans