class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        if len(connections)<n-1:
            return -1
        
        compToNode = defaultdict(list)
        nodeToComp = defaultdict(int)
        currComp = redundantConn = 0
        
        for u,v in connections:
            if u in nodeToComp and v in nodeToComp:
                if nodeToComp[u]==nodeToComp[v]:
                    redundantConn += 1
                    continue
                lComp = min(nodeToComp[u],nodeToComp[v])
                hComp = max(nodeToComp[u],nodeToComp[v])
                
                while compToNode[hComp]:
                    node = compToNode[hComp].pop()
                    nodeToComp[node] = lComp
                    compToNode[lComp].append(node)
            
            elif u in nodeToComp:
                nodeToComp[v] = nodeToComp[u]
                compToNode[nodeToComp[u]].append(v)
            
            elif v in nodeToComp:
                nodeToComp[u] = nodeToComp[v]
                compToNode[nodeToComp[v]].append(u)
            
            else:
                currComp += 1
                nodeToComp[u] = nodeToComp[v] = currComp
                compToNode[currComp].extend([u,v])
        
        # unconnected - lonely count not seen + compToNode (non empty keys)
        unconnected = 0
        for v in compToNode.values():
            if v:
                unconnected += 1
        unconnected += n-len(nodeToComp.keys())
        return unconnected-1 if unconnected-1<=redundantConn else -1