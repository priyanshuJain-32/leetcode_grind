class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n==1:
            return 0
        a = n//2
        return self.numberOfMatches(a) + n%2 + a