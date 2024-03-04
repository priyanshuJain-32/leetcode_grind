class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # Community
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]
        
        # Mine
        # adjacencyL = defaultdict(list)
        # maxi = 0
        # for u,v in edges:
        #     maxi = max(u,v,maxi)
        #     adjacencyL[u].append(v)
        #     adjacencyL[v].append(u)
        # for k,v in adjacencyL.items():
        #     if len(v)==maxi-1:
        #         return k