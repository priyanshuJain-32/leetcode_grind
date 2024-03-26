class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        if m==1 and n==1:
            return grid[0][0]*4
        if m==1:
            ans+= grid[0].count(1)*4
            for i in range(n):
                if grid[0][i]==1:
                    if i==0:
                        ans -= grid[0][i+1]
                    elif i==n-1:
                        ans -= grid[0][i-1]
                    else:
                        ans -= (grid[0][i-1]+grid[0][i+1])
            return ans
        if n==1:
            temp = []
            for i in range(m):
                temp.append(grid[i][0])
            ans += temp.count(1)*4
            for j in range(m):
                if temp[j]==1:
                    if j==0:
                        ans -= temp[j+1]
                    elif j==m-1:
                        ans -= temp[j-1]
                    else:
                        ans -= (temp[j-1]+temp[j+1])
            return ans


        for i in range(m):
            ans += grid[i].count(1)*4
            for j in range(n):
                if grid[i][j]==1:
                    if j==0:
                        ans -= grid[i][j+1]
                    elif j==n-1:
                        ans -= grid[i][j-1]
                    else:
                        ans -= (grid[i][j-1]+grid[i][j+1])
        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(grid[j][i])
            for j in range(m):
                if temp[j]==1:
                    if j==0:
                        ans -= temp[j+1]
                    elif j==m-1:
                        ans -= temp[j-1]
                    else:
                        ans -= (temp[j-1]+temp[j+1])
        return ans