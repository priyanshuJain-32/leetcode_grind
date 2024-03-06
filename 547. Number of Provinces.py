class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def adjL(isConnected, n):
            adj = defaultdict(list)
            for i in range(n):
                for j in range(i+1, n):
                    if isConnected[i][j]==1:
                        adj[i].append(j)
                        adj[j].append(i)
            return adj

        def bfs(adj, start_v, n):
            q = []
            visited = {k:False for k in range(n)}
            visited[start_v] = True
            q.append(start_v)
            while q:
                node = q.pop()
                for j in adj[node]:
                    if not visited[j]:
                        visited[j]=True
                        q.append(j)
            return visited

        n = len(isConnected)

        seen = 0
        adj = adjL(isConnected, n)
        compid = {k:-1 for k in range(n)}
        curr_compid = 0
        while seen<n:
            next_v = min([v for v in range(n) if compid[v]==-1])
            visited = bfs(adj, next_v, n)

            for k,v in visited.items():
                if v==True:
                    compid[k]=curr_compid
                    seen += 1
            curr_compid += 1
        return curr_compid