class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        def listToAList():
            AList = defaultdict(list)
            for u,v in richer:
                AList[u].append(v)
            return AList
        
        def topSort(AList):
            ret = [[i,quiet[i]] for i in range(len(quiet)) ]
            indegree = [0 for _ in range(len(quiet))]

            for u,v in richer:
                indegree[v] += 1
            
            zeroQueue = deque()
            
            for u,i in enumerate(indegree):
                if i==0:
                    
                    zeroQueue.append(u)
                    
            while zeroQueue:
                curr = zeroQueue.pop()

                indegree[curr] -= 1
                
                for node in AList[curr]:
    
                    if ret[curr][1]<ret[node][1]:
                        ret[node]=[ret[curr][0],ret[curr][1]]
                    indegree[node] -= 1
                    if indegree[node]==0:
                        zeroQueue.append(node)
            
            return [i for i,j in ret]

        return topSort(listToAList())