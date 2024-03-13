class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = [""]*len(s)
        for c,i in zip(s,indices):
            ans[i] = c
        return "".join(ans)