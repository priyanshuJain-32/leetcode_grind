class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def generate(node, closed):
            path = []
            while node!=-1:
                path.append(node)
                node = closed[node]
            
            return path[::-1]

        op = [(0,-1)]
        closed = defaultdict(int)
        dest = len(graph)-1
        paths = []
        while op:
            node, parent = op.pop()
            closed[node] = parent
            if node==dest:
                paths.append(generate(node, closed))
            else:
                for v in graph[node]:
                    op.append((v,node))
        return paths