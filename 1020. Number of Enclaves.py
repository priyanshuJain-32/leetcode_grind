class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    grid[i][j] = 0
                    count += self.dfs(grid,i,j,m,n)
        return count
    def dfs(self,grid,i,j,m,n):
        queue = [(i,j)]
        flag = False
        count = 0
        while queue:
            count +=1
            I,J = queue.pop()
            if I==0 or I==m-1 or J==0 or J==n-1:
                flag = True
            for r,c in (I+1,J),(I-1,J),(I,J+1),(I,J-1):
                if 0<=r<m and 0<=c<n and grid[r][c]==1:
                    grid[r][c]=0
                    queue.append((r,c))
        if flag:
            return 0
        return count