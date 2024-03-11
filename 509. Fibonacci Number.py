class Solution:
    def fib(self, n: int) -> int:
        F = [0,1]
        if n<2:
            return F[n]
        for i in range(2,n+1):
            F.append(F[i-1]+F[i-2])
        return F[-1]