class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        # traverse the grid2
        # when we find an island add the indices to a list
        # now traverse the list and see if there is a tile with 1 in grid2
        # if even 1 single tile in grid2's island, grid1 is not 1 break the loop
        # otherwise increment count
        
        m,n = len(grid2), len(grid2[0])
        count = 0
        for i in range(m):
            for j in range(n):
                island = []
                if grid2[i][j]==1:
                    grid2[i][j] = 0
                    island.append((i,j))
                    island.extend(self.helper(grid2,i,j,m,n))
                    flag = True
                    for (a,b) in island:
                        if grid1[a][b]==0:
                            flag = False
                            break
                    if flag:
                        count += 1
        return count

    def helper(self, grid2,i,j,m,n):
        que = [(i,j)]
        land = []
        while que:
            r,c = que.pop()
            for (a,b) in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if 0<=a<m and 0<=b<n and grid2[a][b]==1:
                    grid2[a][b]=0
                    land.append((a,b))
                    que.append((a,b))
        return land