class Solution:
    def checkIfPrerequisite(self, nC: int, pR: List[List[int]], queries: List[List[int]]) -> List[bool]:
        aList = defaultdict(list)
        
        pre = defaultdict(set)

        indirect = [0]*nC
        
        for u,v in pR:
            indirect[v] += 1
            aList[u].append(v)
        
        zeroQ = deque([i for i in range(nC) if not indirect[i]])

        while zeroQ:
            curr = zeroQ.popleft()
            indirect[curr] -= 1

            for node in aList[curr]:
                indirect[node] -= 1
                if indirect[node]==0:
                    zeroQ.append(node)
                
                pre[node].add(curr)
                if curr in pre:
                    for n in pre[curr]:
                        pre[node].add(n)
        ret = []
        for u,v in queries:
            if v not in pre:
                ret.append(False)
                continue
            if u not in pre[v]:
                ret.append(False)
                continue
            ret.append(True)

        return ret