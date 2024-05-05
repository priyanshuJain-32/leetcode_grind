class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        # I will mark the paths with numbers and keep a count of paths
        # There should be only 1 path for true
        m, n = len(grid),len(grid[0])
        path1 = self.dfs(grid,m,n)
        if not path1:
            return True
        grid[0][0] = 1
        grid[-1][-1] = 1
        path2 = self.dfs(grid,m,n)
        return not path2
        
    def dfs(self,grid,m,n):
        queue = [(0,0)]
        while queue:
            r,c = queue.pop()
            grid[r][c] = 0
            if (r,c)==(m-1,n-1):
                return True
            for I,J in (r,c+1),(r+1,c):
                if 0<=I<m and 0<=J<n and grid[I][J]==1:
                    queue.append((I,J))
        return False

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        m, n = len(grid),len(grid[0])
        # backward pruning
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i==m-1 and j!=n-1:
                    if grid[i][j+1]==0:
                        grid[i][j]=0

                elif i!=m-1 and j==n-1:
                    if grid[i+1][j]==0:
                        grid[i][j]=0

                elif i!=m-1 and j!=n-1:
                    if grid[i+1][j]==0 and grid[i][j+1]==0:
                        grid[i][j]=0

        # forward pruning
        for i in range(m):
            for j in range(n):
                if i==0 and j!=0:
                    if grid[i][j-1]==0:
                        grid[i][j]=0
                elif i!=0 and j==0:
                    if grid[i-1][j]==0:
                        grid[i][j]=0
                elif i!=0 and j!=0:
                    if grid[i-1][j]==0 and grid[i][j-1]==0:
                        grid[i][j]=0
                
        # calculate diagonal totals
        diag = [0]*(m+n-1)
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    diag[i+j]+=1
        # if any diagonal is 1 or less in total return True
        for i in range(1,m+n-2):
            if diag[i]<2:
                return True

        # else return False
        return False





    # Failed in trying double dfs earlier    
    #     if (m==1 and n>2) or (m>2 and n==1):
    #         return True
    #     if m==2 and n==2:
    #         return True
    #     if (m==1 and n<=2) or (m<=2 and n==1):
    #         return False
    #     comp = 2
    #     count = 0
    #     flagRight = flagDown = False
    #     if grid[0][1]==1:
    #         grid[0][1]=2
    #         flagRight = self.dfs(grid,0,1,m,n,2,True)
    #     grid[m-1][n-1]=1
    #     if grid[1][0]==1:
    #         grid[1][0]=3
    #         flagDown = self.dfs(grid,1,0,m,n,3,False)
    #     # print(grid)
    #     if flagRight and flagDown:
    #         return False
    #     return True
    
    # def dfs(self,grid,i,j,m,n,comp,right):
    #     queue = [(i,j)]
    #     flag = False
    #     while queue:
    #         r,c = queue.pop()
    #         if right:
    #             for I,J in (r,c+1),(r+1,c):
    #                 if 0<=I<m and 0<=J<n and grid[I][J]==1:
    #                     if (I,J) == (m-1,n-1):
    #                         flag = True
    #                     grid[I][J]=comp
    #                     queue.append((I,J))
    #                     break
    #         else:
    #             for I,J in (r+1,c),(r,c+1):
    #                 if 0<=I<m and 0<=J<n and grid[I][J]==1:
    #                     if (I,J) == (m-1,n-1):
    #                         flag = True
    #                     grid[I][J]=comp
    #                     queue.append((I,J))
                        

    #     return flag

    # # [1,1,0,0,0,0],
    # # [1,1,1,1,1,1],
    # # [1,1,1,1,1,1],
    # # [1,1,1,1,0,1],
    # # [0,0,0,1,1,1],
    # # [0,0,0,1,0,1],
    # # [0,0,0,1,0,1],
    # # [0,0,0,1,0,1],
    # [0,0,0,1,0,1],
    # [0,0,0,1,1,1]