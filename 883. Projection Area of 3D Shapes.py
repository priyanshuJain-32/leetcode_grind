class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        cx = cy = cz = 0
        for i in range(n):
            max_grid = 0
            temp = []
            for j in range(n):
                if grid[i][j]>max_grid:
                    max_grid = grid[i][j]
                if grid[i][j]!=0:
                    cz+=1
                temp.append(grid[j][i])
            cy += max(temp)
            cx += max_grid
        return cx+cy+cz