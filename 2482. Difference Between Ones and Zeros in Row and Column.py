class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        scoresRow, scoresCol = [0]*m, [0]*n
        
        for r in range(m):
            scoresRow[r] = 2*sum(grid[r]) - m
        
        for c in range(n):
            for r in range(m):
                scoresCol[c] += grid[r][c]
            scoresCol[c] = 2*scoresCol[c] - n
        
        for r in range(m):
            for c in range(n):
                grid[r][c] = scoresRow[r] + scoresCol[c]
        return grid
