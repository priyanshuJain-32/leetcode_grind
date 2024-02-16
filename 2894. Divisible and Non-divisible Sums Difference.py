class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return int((n+1)*n/2-(n//m+1)*(n//m)*m)