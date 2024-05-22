class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Create two dictionaries to keep track of
        compToNode = defaultdict(list) # which component has what nodes
        nodeComp = defaultdict(int) # which nodes are in what components
        currComp = 0 # current component
        for u,v in edges: # For each edge
            
            if u in nodeComp and v in nodeComp: # if both the nodes have a component number
                if nodeComp[u]==nodeComp[v]: # if both are same
                    return [u,v] # then we have a cycle on this edge
            
                lComp = min(nodeComp[u],nodeComp[v]) # otherwise find the lesser comp number
                hComp = max(nodeComp[u],nodeComp[v]) # and higher comp number
            
                nodeComp[v] = nodeComp[u] = lComp # change the comp number of both to lower one
            
                while compToNode[hComp]: # also change comp number of each higher comp to lower comp as they are now connected
                    node = compToNode[hComp].pop() # pop the node
                    nodeComp[node] = lComp # give lower comp number
                    compToNode[lComp].append(node) # append it to the lower comp list
            
            elif u in nodeComp: # if only start is there then 
                nodeComp[v] = nodeComp[u] # give end the same comp
                compToNode[nodeComp[u]].append(v) # and add this end to list
            
            elif v in nodeComp: # if only end is there then
                nodeComp[u] = nodeComp[v] # give start the same comp as end
                compToNode[nodeComp[v]].append(u) # and add this start to list
            
            else: # if both are not there then we have new component
                currComp += 1 # increment currComp
                nodeComp[u] = nodeComp[v] = currComp # give both start and end this number
                compToNode[currComp].extend([u,v]) # append these to the list