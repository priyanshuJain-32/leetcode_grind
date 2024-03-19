class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in grid:
            i.sort()
        m,n = len(grid), len(grid[0])
        ans = 0
        for i in range(n):
            col = []
            for j in range(m):
                col.append(grid[j][i])
            ans += max(col)
        return ansg