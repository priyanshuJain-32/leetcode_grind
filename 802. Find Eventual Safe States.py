class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = [0]*n
        adj = [[] for _ in range(n)]

        for i in range(n):
            for node in graph[i]:
                adj[node].append(i)
                indegree[i] += 1

        q = deque()
        for i in range(n):
            if indegree[i]==0:
                q.append(i)
        
        safe = [False]*n
        while q:
            node = q.popleft()
            safe[node] = True

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor]==0:
                    q.append(neighbor)
        
        safeNodes = []
        for i in range(n):
            if safe[i]:
                safeNodes.append(i)

        return safeNodes


        
        # terminal = {i for i in range(len(graph)) if not graph[i]}
        # safe = {k:False for k in range(len(graph)) if k not in terminal}
        
        # def dfs(source):
        #     stack = [source]
        #     visited = {0}

        #     for t in terminal:
        #         visited.add(t)
            
        #     while stack:
            
        #         source = stack[-1]
        #         if all(dest in terminal or (dest in safe and safe[dest]==True) for dest in graph[source]):
        #             safe[source] = True
                    
        #         if all(dest in visited for dest in graph[source]):
        #             stack.pop()
        #             continue
                
        #         for dest in graph[source]:
        #             if dest not in visited:
        #                 visited.add(dest)
        #                 stack.append(dest)
                    
        # for i in range(len(graph)): 
        #     if i not in terminal:
        #         if not safe[i]:
        #             dfs(i)
        
        # ans = [k for k,v in safe.items() if v==True]
        
        # for t in terminal:
        #     ans.append(t)

        # return sorted(ans)