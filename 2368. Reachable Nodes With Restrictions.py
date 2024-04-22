class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        self.restricted = set(restricted)
        self.adjacencyList(n,edges)
        visited = {0}
        opn = [0]
        cnt = 0
        while opn:
            node = opn.pop()
            cnt += 1
            for v in self.aL[node]:
                if v not in visited:
                    visited.add(v)
                    opn.append(v)

        return cnt

    def adjacencyList(self,n,edges):
        self.aL = defaultdict(list)
        for s,e in edges:
            if s not in self.restricted and e not in self.restricted:
                self.aL[s].append(e)
                self.aL[e].append(s)