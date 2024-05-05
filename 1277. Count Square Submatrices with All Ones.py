class Solution:
    def countSquares(self, grid: List[List[int]]) -> int:
        count = 0
        m,n = len(grid),len(grid[0])
        
        for i in range(m):
            if grid[i][0]==1:
                count +=1
        
        for j in range(1,n):
            if grid[0][j]==1:
                count += 1
        
        for i in range(1,m):
            for j in range(1,n):
                if grid[i][j]==1:
                    grid[i][j] = min(grid[i-1][j-1],grid[i][j-1],grid[i-1][j])+1
                    count += grid[i][j]
        return count