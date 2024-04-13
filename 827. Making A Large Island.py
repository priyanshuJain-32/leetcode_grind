class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        comp = 2
        self.comp_area = {}
        m,n = len(grid), len(grid[0])
        
        flag = False
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    grid[i][j] = comp
                    area = self.helper(grid,i,j,m,n,comp)
                    self.comp_area[comp] = area
                    comp+=1
                elif grid[i][j]==0:
                    flag = True
        if not flag:
            return m*n
        
        return self.find(grid,m,n)+1

    def find(self,grid,m,n):
        max_area = 0
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j]==0:
                    f1x,f1y = (i+1,j)
                    f2x,f2y = (i-1,j)
                    f3x,f3y = (i,j+1)
                    f4x,f4y = (i,j-1)
                    temp = set()
                    if 0<=f1x<m and 0<=f1y<n and grid[f1x][f1y]!=0 and grid[f1x][f1y]!=1:
                        temp.add(grid[f1x][f1y])
                    if 0<=f2x<m and 0<=f2y<n and grid[f2x][f2y]!=0 and grid[f2x][f2y]!=1:
                        temp.add(grid[f2x][f2y])
                    if 0<=f3x<m and 0<=f3y<n and grid[f3x][f3y]!=0 and grid[f3x][f3y]!=1:
                        temp.add(grid[f3x][f3y])
                    if 0<=f4x<m and 0<=f4y<n and grid[f4x][f4y]!=0 and grid[f4x][f4y]!=1:
                        temp.add(grid[f4x][f4y])
                    temp_area = 0
                    for k in temp:
                        temp_area += self.comp_area[k]
                    max_area = max(temp_area, max_area)
        return max_area

    def helper(self,grid,i,j,m,n,comp):
        que = [(i,j)]
        area = 1
        while que:
            r,c = que.pop()
            for i,j in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0<=i<m and 0<=j<n and grid[i][j]==1:
                    que.append((i,j))
                    grid[i][j] = comp
                    area += 1
        return area
    # a large island is far from smaller islands
    # a large island is close to small island
    # a large island is close more than 1 small island with different sizes
    # two smaller islands are closer to each other and can make a larger island than a large island and another small island

    # Need to create sort of a brige, if changing one point connects them then the second point will definitely be inside the other island

    # the second point will be neighbour of the point which is going to be changed 

    # which area combination will give highest area
	# multiple combo cases