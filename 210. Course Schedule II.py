class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        aList = defaultdict(list)
        indegree = [0]*numCourses
        zeroQ = deque()

        for u,v in prerequisites:
            aList[v].append(u)
            indegree[u]+=1
        
        for node, indeg in enumerate(indegree):
            if indeg==0:
                zeroQ.append(node)
        ret = []
        while zeroQ:
            curr = zeroQ.popleft()
            indegree[curr] -= 1
            
            ret.append(curr)

            for node in aList[curr]:
                indegree[node]-=1

                if indegree[node]==0:
                    zeroQ.append(node)
        
        return ret if len(ret)==numCourses else []