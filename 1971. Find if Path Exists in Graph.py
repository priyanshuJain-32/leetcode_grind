class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.adjacencyL = {k:[] for k in range(n)}
        def adjacencyList(L, n):
            for i,j in L:
                self.adjacencyL[i].append(j)
                self.adjacencyL[j].append(i)
        adjacencyList(edges, n)
        open = [source]
        seen = {source}
        while open:
            node = open.pop(-1)
            if node==destination:
                return True
            for v in self.adjacencyL[node]:
                if v not in seen:
                    seen.add(v)
                    open.append(v)
        return False