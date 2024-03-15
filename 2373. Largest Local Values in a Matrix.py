class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0]*(n-2) for _ in range(n-2)]
        
        k = 0
        while k<n-2:
            for j in range(n):
                grid[j][k] = max(grid[j][k:k+3])
            k += 1
       
	k = 0
        while k<n-2:
            for i in range(n-2):
                l = []
                for j in range(k,k+3):
                    l.append(grid[j][i])
                
                ans[k][i] = max(l)
            k+=1
        return ans