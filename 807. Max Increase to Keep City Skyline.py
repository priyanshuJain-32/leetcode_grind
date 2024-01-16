class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        west_east_skl = []
        north_south_skl = []
        n = len(grid)
        for i in range(n):
            west_east_skl.append(max(grid[i]))
            skl = 0
            for j in range(n):
               skl = max(skl, grid[j][i])
            north_south_skl.append(skl)
        ret = 0
        for i in range(n):
            for j in range(n):
                ret+=min(north_south_skl[j], west_east_skl[i])-grid[i][j]
        return ret
