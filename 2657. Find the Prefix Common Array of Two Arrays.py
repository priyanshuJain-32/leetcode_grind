class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        ans = [0]*n
        for i in range(n):
            ans[i] = 2*(i+1) - len(set(A[:i+1]+B[:i+1]))
        return ans