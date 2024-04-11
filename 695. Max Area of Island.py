class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    grid[i][j]=0
                    area = max(area,self.helper(grid,i,j,m,n))
        return area
    def helper(self,grid,i,j,m,n):
        que = [(i,j)]
        area = 1
        while que:
            i,j = que.pop()
            for r,c in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                if 0<=r<m and 0<=c<n and grid[r][c]==1:
                    area += 1
                    grid[r][c]=0
                    que.append((r,c))
        return area