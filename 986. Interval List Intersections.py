class Solution:
    def intervalIntersection(self, fL: List[List[int]], sL: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        m,n = len(fL), len(sL)
        ans = []
        while i<m and j<n:
            a1,b1 = fL[i]
            a2,b2 = sL[j]
            if a1>b2:
                j+=1
            elif b1<a2:
                i+=1
            else:
                ans.append([max(a1,a2),min(b1,b2)])
                if b1>b2:
                    j+=1
                else:
                    i+=1
        return ans