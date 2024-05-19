class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
    # Main logic
    # Run through the edges and create a Adjacency List
    # Iterate from 0 to n-1 and run bfs on the node if it has not been visited
    # While performing bfs put all the nodes in the component
    # For each node in component the nodes in adjacency list should be #components-1
    # if for any of the node it is not then that component is not complete
    # if some node has nothing in adjacency list that means it is alone and its #components-1=0
    
    # Create Adjacency List
        self.aL = defaultdict(list)
        self.aList(edges)

        self.visited = set()
        
        ans = 0
        for u in range(n):
            if u not in self.visited:
                component = self.bfs(u)
                flag = True
                for node in component:
                    if len(component)-1!=len(self.aL[node]):
                        flag = False
                if flag:
                    ans += 1
        return ans


    def aList(self,edges):
        for u,v in edges:
            self.aL[u].append(v)
            self.aL[v].append(u)
    
    
    def bfs(self,source):
        queue = deque([source])
        component = set([source])
        while queue:
            node = queue.popleft()
            self.visited.add(node)
            for v in self.aL[node]:
                if v not in self.visited:
                    self.visited.add(v)
                    queue.append(v)
                    component.add(v)
        return component