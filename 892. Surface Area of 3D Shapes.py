class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        m = len(grid)
        left,right,up,down,top,bottom = 0,0,0,0,0,0
        ans = 0
        for i in range(m):
            for j in range(m):
                if i==0:
                    up = grid[i][j]
                else:
                    up = max(0,grid[i][j]-grid[i-1][j])
                if i==m-1:
                    down = grid[i][j]
                else:
                    down = max(0,grid[i][j] - grid[i+1][j])
                if j==0:
                    left = grid[i][j]
                else:
                    left = max(0,grid[i][j]-grid[i][j-1])
                if j==m-1:
                    right = grid[i][j]
                else:
                    right = max(0,grid[i][j]-grid[i][j+1])
                if grid[i][j]!=0:
                    top = 1
                    bottom = 1
                else:
                    top = 0
                    bottom = 0
                ans += top+bottom+left+right+up+down
        return ans