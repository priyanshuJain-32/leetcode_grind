class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n<2:
            return 1
        def slope(p1, p2):
            try:
                return (p2[1]-p1[1])/(p2[0]-p1[0])
            except:
                return "inf"
        lines = 1
        for i in range(n-1):
            D = {}
            for j in range(i+1, n):
                s = slope(points[j], points[i])
                D[s] = 1 + D.get(s,0)
            lines = max(lines, max(D.values()))
        return lines + 1
