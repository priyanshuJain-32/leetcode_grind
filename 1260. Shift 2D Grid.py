class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(grid),len(grid[0])
        array = deque([grid[x][y] for x in range(m) for y in range(n)])
        while k>0:
            array.appendleft(array.pop())
            k-=1
        l = 0
        for i in range(m):
            for j in range(n):
                grid[i][j] = array[l]
                l+=1
        return grid