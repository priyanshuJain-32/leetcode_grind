class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [set() for _ in range(n)]
        def listToAList():
            AList = defaultdict(list)
            for u,v in edges:
                AList[u].append(v)
            return AList
        def topSort(AList):
            indegree = [0 for _ in range(n)]

            for u,v in edges:
                indegree[v] += 1
            
            zeroQueue = deque()
            for node, indeg in enumerate(indegree):
                if indeg == 0:
                    zeroQueue.append(node)
            
            while zeroQueue:
                curr = zeroQueue.pop()
                indegree[curr] -= 1

                for node in AList[curr]:
                    indegree[node] -= 1
                    ans[node].add(curr)
                    for i in ans[curr]:
                        ans[node].add(i)
                    
                    if indegree[node]==0:
                        zeroQueue.append(node)

        topSort(listToAList())
        return [sorted(i) for i in ans]