class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # DP way
        table = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                table[i][j] = table[i-1][j]+table[i][j-1]
        return table[m-1][n-1]

        # Mathematical approach
        # self.f = {1:1,0:1}
        # def fact(n):
        #     if n in self.f:
        #         return self.f[n]
        #     self.f[n] = n*fact(n-1)
        #     return self.f[n]
        # return int(fact(m+n-2)/(fact(n-1)*fact(m-1)))