class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        def rowSwap(grid,m,n):
            for i in range(m):
                if grid[i][0]==0:
                    for j in range(n):
                        grid[i][j] = int(grid[i][j]==0)
        def colSwap(grid,m,n):
            for j in range(n):
                count = 0
                for i in range(m):
                    count += grid[i][j]
                if count<m/2:
                    for i in range(m):
                        grid[i][j] = int(grid[i][j]==0)
        
        def total(grid,m,n):
            ans = 0
            for i in range(m):
                ans += int("".join(list(map(str,grid[i]))),2)
            return ans

        m,n = len(grid),len(grid[0])
        rowSwap(grid,m,n)
        colSwap(grid,m,n)
        return total(grid,m,n)