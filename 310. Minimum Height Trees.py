class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # There is a trick here
        # We need to prune the nodes with one connected edge
        degree = [0]*n # indegree + outdegree
        aList = defaultdict(list)

        for u,v in edges:
            aList[u].append(v)
            aList[v].append(u)
            degree[u] += 1
            degree[v] += 1
        leaves = []
        # If indegree is 1 then the node is a leaf
        for node,deg in enumerate(degree):
            if deg==1:
                leaves.append(node)
        
        while n>2:
            n-=len(leaves) # reduce the total leaves
            newLeaves = []

            for leaf in leaves:
                degree[leaf] -= 1
            
                for node in aList[leaf]:
                    degree[node] -= 1
            
                    if degree[node]==1:
                        newLeaves.append(node)
            
            leaves = newLeaves
            
        return leaves if leaves else [0]