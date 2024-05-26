class Solution:
    def canFinish(self, nC: int, prereq: List[List[int]]) -> bool:
        aList = defaultdict(list)
        indegree = [0]*nC
        for u,v in prereq:
            aList[v].append(u)
            indegree[u] += 1

        zeroQ = deque([i for i in range(nC) if not indegree[i]])

        sequence = []
        while zeroQ:

            curr = zeroQ.popleft()
            indegree[curr] -= 1
            
            sequence.append(curr)
            
            for node in aList[curr]:
                indegree[node] -= 1
            
                if indegree[node] == 0:
                    zeroQ.append(node)
        
        return len(sequence)==nC

        
            
