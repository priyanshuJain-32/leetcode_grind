class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    grid[i][j]=0
                    self.helper(grid,i,j,m,n)
                    count += 1
        return count
    def helper(self,grid,i,j,m,n):
        que = [(i,j)]
        while que:
            x,y = que.pop()
            for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                r,c = x+dr,y+dc
                if 0<=r<m and 0<=c<n and grid[r][c]=="1":
                    grid[r][c]=0
                    que.append((r,c))