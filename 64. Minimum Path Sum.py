class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        table = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    table[i][j] = grid[i][j]
                    continue
                elif i==0 and j!=0:
                    table[i][j] += table[i][j-1]+grid[i][j]
                    continue
                elif i!=0 and j==0:
                    table[i][j] += table[i-1][j]+grid[i][j]
                    continue
                table[i][j] += min(table[i-1][j], table[i][j-1])+grid[i][j]
        return table[m-1][n-1]