class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = defaultdict(dict)
        for i in range(len(equations)):
            d[equations[i][0]][equations[i][1]] = values[i]
            d[equations[i][1]][equations[i][0]] = 1/values[i]

        def bfs(source, destination):
            queue = deque([(source,"#")])
            closed = defaultdict(str)
            parent = "#"
            while queue:
                node,parent = queue.popleft()
                closed[node] = parent
                if node==destination:
                    return constructPath(closed,source,destination)
                if node in d:
                    for neighbor in d[node]:
                        if neighbor not in queue and neighbor not in closed:
                            queue.append((neighbor,node))
            return ""
        
        def constructPath(closed,source,destination):
            curr = destination
            path = destination
            while curr!=source:
                path = closed[curr] + ","+ path
                curr = closed[curr]
            return path
        
        ans = []
        for source,destination in queries:
            if source==destination and source in d:
                ans.append(round(1,5))
                continue
            result = bfs(source,destination).split(",")
            
            if result==[''] or len(result)==1:
                ans.append(round(-1,5))
            else:
                output = 1
            
                for i in range(len(result)-1):
                    output *= d[result[i]][result[i+1]]
            
                ans.append(round(output,5))
        return ans