class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        component = {}
        n = len(points)
        for i in range(n-1):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                cost = abs(x1-x2) + abs(y1-y2)
                edges.append((cost, i, j))
                component[i] = i
                component[j] = j
        edges.sort()
        dist = 0
        for d,u,v in edges:
            if component[u]!=component[v]:
                c = component[u]
                dist += d
                for w in range(n):
                    if component[w]==c:
                        component[w] = component[v]
        return dist