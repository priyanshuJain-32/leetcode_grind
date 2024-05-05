class Solution:
    def maximalSquare(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        result = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    result = 1
        
        for i in range(1,m):
            for j in range(1,n):
                if grid[i][j]=="1":
                    grid[i][j] = min(int(grid[i-1][j-1]),int(grid[i][j-1]),int(grid[i-1][j]))+1
                    if grid[i][j]>result:
                        result = grid[i][j]
        return result**2

    # All the wrong ways
    #     for i in range(m):
    #         for j in range(n):
    #             flag = False
    #             for ((r1,c1),(r2,c2)) in [((i+1,j),(i,j+1)),((i+1,j),(i,j-1)), ((i-1,j),(i,j+1)),((i-1,j),(i,j-1))]:
    #                 if 0<=r1<m and 0<=c1<n and 0<=r2<m and 0<=c2<n:
    #                     if (grid[r1][c1]=="1" and grid[r2][c2]=="1"):
    #                         flag = True
    #             if not flag:
    #                 grid[i][j] = "0"

    #     for i in range(m-1,-1,-1):
    #         for j in range(n-1,-1,-1):
    #             flag = False
    #             for ((r1,c1),(r2,c2)) in [((i+1,j),(i,j+1)),((i+1,j),(i,j-1)), ((i-1,j),(i,j+1)),((i-1,j),(i,j-1))]:
    #                 if 0<=r1<m and 0<=c1<n and 0<=r2<m and 0<=c2<n:
    #                     if (grid[r1][c1]=="1" and grid[r2][c2]=="1"):
    #                         flag = True
    #             if not flag:
    #                 grid[i][j] = "0"
    #     # print(grid)
    #     self.dims = defaultdict(list)
    #     comp = 1
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j]=="1":
    #                 self.dfs(grid,i,j,m,n,comp)

    #     return 0
    # def dfs(self,grid,i,j,m,n,comp):
    #     queue = [(i,j)]
    #     xmin,xmax,ymin,ymax = 0,0,0,0
    #     while queue:
    #         r,c = queue.pop()
    #         for I,J in (r+1,c),(r-1,c),(r,c+1),(r,c-1):
    #             if 0<=I<m and 0<=J<n and grid[I][J]=="1":
    #                 grid[I][J] = comp
    #                 queue.append((I,J))
    #                 xmin,xmax = min(xmin,I),max(xmax,I)
    #                 ymin,ymax = min(ymin,J),max(ymax,J)


    #             # if i==0 and j==0:
    #             #     if not (grid[i+1][j] and grid[i][j+1]):
    #             #         grid[i][j] = 0
                    
    #             # elif i==0 and j==n-1:
    #             #     if not (grid[i][j-1] and grid[i+1][j]):
    #             #         grid[i][j] = 0
                
    #             # elif i==m-1 and j==0:
    #             #     if not (grid[i-1][j] and grid[i][j+1]):
    #             #         grid[i][j] = 0
                
    #             # elif i==m-1 and j==n-1:
    #             #     if not (grid[i-1][j] and grid[i][j-1]):
    #             #         grid[i][j] = 0
                
    #             # elif i==0:
    #             #     if not (grid[i][j-1] and grid[i+1][j]) and not (grid[i][j+1] and grid[i+1][j]):
    #             #         grid[i][j] = 0
                
    #             # elif i==

