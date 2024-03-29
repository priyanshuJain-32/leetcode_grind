class Solution:
    def countBits(self, n: int) -> List[int]:
        l = [0]*(n+1)
        for i in range(1,n+1):
            l[i] = l[i//2] + i%2
        return l