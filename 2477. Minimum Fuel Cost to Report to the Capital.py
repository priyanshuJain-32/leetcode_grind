class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # First convert into adjacency list
        aList = defaultdict(list)
        for origin,destination in roads:
            aList[origin].append(destination)
            aList[destination].append(origin)
        
        # Next we will run a dfs with curr and prev
        # For each child of curr we will calculate total of people
        # on that node and calculate cost till then
        

        def dfs(curr,prev):
            people = 1
            for nxt in aList[curr]:
                if nxt == prev: continue
                people += dfs(nxt,curr)
            self.ans += int(math.ceil(people/seats)) if curr else 0
            return people
        
        self.ans = 0
        dfs(0,0)
        return self.ans
        # visited = defaultdict(bool)
        # def adjList(roads):
        #     WList = defaultdict(list)
        #     for u,v in roads:
        #         WList[u].append(v)
        #         WList[v].append(u)
        #         visited[u]=False
        #         visited[v]=False
        #     return WList
        # WList = adjList(roads)
        # q = deque()
        # q.append(0)
        # visited[0] = True
        # paths = []
        # path = ""
        # # print(q)
        # while q:
        #     node = q.pop()
        #     count = 0
        #     path += str(node)
        #     for v in WList[node]:
        #         if not visited[v]:
        #             count += 1
        #             visited[v] = True
        #             q.append(v)
        #     if count==0:
        #         paths.append(path)
        #         path = path[:-1]
        # total = 0
        # print(paths)
        # for i in paths:
        #     n = len(i)-1
        #     print(n)
        #     if n>seats:
        #         idx = n
        #         while idx>-1:
        #             total += idx
        #             idx -= seats
        #     else:
        #         total += n
        # return total