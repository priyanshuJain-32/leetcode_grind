class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        degrees = {k:[0,0] for k in range(n)}
        for u,v in edges:
            degrees[u][0]+=1
            degrees[v][1]+=1
        ans = []
        for k,v in degrees.items():
            if v[1]==0:
                ans.append(k)
        return ans

# Improved
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inedges = set()
        for u,v in edges:
            inedges.add(v)
        ans = set()
        for u,v in edges:
            if u not in inedges:
                ans.add(u)
        return list(ans)