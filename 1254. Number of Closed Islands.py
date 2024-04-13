class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        count = 0
        for i in range(1,m-1):
            for j in range(1,n-1):
                flag = False
                if grid[i][j]==0:
                    grid[i][j]=1
                    flag = self.check(grid,i,j,m,n)
                if flag:
                    count += 1
        return count
    def check(self,grid,i,j,m,n):
        que = [(i,j)]
        flag = True
        while que:
            I,J = que.pop()
            for x,y in [(I+1,J),(I-1,J),(I,J-1),(I,J+1)]:
                if 0<=x<m and 0<=y<n and grid[x][y]==0:
                    grid[x][y]=1
                    que.append((x,y))
                    if x==0 or x==m-1 or y==0 or y==n-1:
                        flag = False
        return flag