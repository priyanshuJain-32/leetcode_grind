class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m,n = len(land),len(land[0])
        ans = []
        for i in range(m):
            for j in range(n):
                temp = []
                if land[i][j]==1:
                    land[i][j]=0
                    island = self.helper(land,i,j,m,n)
                    island.sort()
                    temp.extend(island[0])
                    temp.extend(island[-1])
                if temp:
                    ans.append(temp)
        return ans

    def helper(self,land,i,j,m,n):
        que = [(i,j)]
        island = [(i,j)]
        while que:
            x,y = que.pop()
            for a,b in [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]:
                if 0<=a<m and 0<=b<n and land[a][b]==1:
                    land[a][b]=0
                    island.append((a,b))
                    que.append((a,b))
        return island