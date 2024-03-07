class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        edge_count = defaultdict(int)
        edges = defaultdict(list)
        for u,v in roads:
            edge_count[u] += 1
            edge_count[v] += 1
            edges[u].append(v)
            edges[v].append(u)
        ans = 0

        for i in range(n-1):
            for j in range(i+1,n):
                rank = edge_count[i]+edge_count[j]
                if j in edges[i] or i in edges[j]:
                    rank -=1
                ans = max(rank, ans)
        return ans