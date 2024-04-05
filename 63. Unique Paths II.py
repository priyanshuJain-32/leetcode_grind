class Solution:
    def uniquePathsWithObstacles(self, oG: List[List[int]]) -> int:
        if oG[-1][-1] or oG[0][0]:
            return 0
        m,n = len(oG), len(oG[0])
        table = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(0,len(oG)):
            for j in range(0,len(oG[0])):
                if i==0 and j==0:
                    continue
                elif i==0 and j!=0:
                    table[i][j] = table[i][j-1] if oG[i][j-1]==0 else 0
                    continue
                elif i!=0 and j==0:
                    table[i][j] = table[i-1][j] if oG[i-1][j]==0 else 0
                    continue
                a = table[i-1][j] if oG[i-1][j]==0 else 0
                b = table[i][j-1] if oG[i][j-1]==0 else 0
                table[i][j] = a+b
        return table[m-1][n-1]
