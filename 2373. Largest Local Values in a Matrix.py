class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        m,n = len(grid),len(grid[0])
        ans = [[0 for _ in range(n-2)] for _ in range(m-2)]
        for i in range(1,m-1):
            for j in range(1,n-1):
                ans[i-1][j-1] = max(max(grid[i-1][j-1:j+2]),max(grid[i][j-1:j+2]),max(grid[i+1][j-1:j+2]))
        return ans