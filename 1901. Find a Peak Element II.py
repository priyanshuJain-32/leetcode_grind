class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        
        # (O(mlogm))
        def rowPeak(mat,i):
            peak = 0
            peakIdx = 0
            for idx,m in enumerate(mat[i]):
                if m>peak:
                    peak = m
                    peakIdx = idx
            return peak,peakIdx
        
        l = j = 0
        r = len(mat)-1

        while l<=r:
            m = (l+r)//2
            peak,j = rowPeak(mat,m)

            try:
                if peak<mat[m+1][j]:
                    l = m+1
                else:
                    r = m-1
            except:
                break

        return [l,j]
        

        

        
        # O(m*n)
        # m,n = len(mat),len(mat[0])
        # for i in range(m):
        #     for j in range(n):
        #         count = 0
        #         for I,J in (i,j+1),(i,j-1),(i+1,j),(i-1,j):
        #             if 0<=I<m and 0<=J<n:
        #                 if mat[i][j]<=mat[I][J]:
        #                     break
        #                 else:
        #                     count += 1
        #             if count == 4:
        #                 return [i,j]
        #             elif count == 3 and ((0<i<m-1 and (j==0 or j==n-1)) or ((i==0 or i==m-1) and 0<j<n-1)):
        #                 return [i,j]
        #             elif count == 2 and (i,j) in [(0,0),(m-1,0),(0,n-1),(m-1,n-1)]:
        #                 return [i,j]
        #             elif count == 1 and (m == 1 or n==1):
        #                 return [i,j]
        #             elif count == 0 and (m,n) == (1,1):
        #                 return [i,j]