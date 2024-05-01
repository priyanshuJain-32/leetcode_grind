class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m,n = len(mat),len(mat[0])
        rowTotals = [[0,0] for _ in range(m)]
        colTotals = [0]*n
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1:
                    rowTotals[i][0] += 1
                    rowTotals[i][1] = j
                    colTotals[j] += 1
                
        count = 0
        for rt in rowTotals:
            if rt[0]==1 and colTotals[rt[1]]==1:
                count += 1
        return count