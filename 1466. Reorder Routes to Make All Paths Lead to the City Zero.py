class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Create a directional AList
        # Create a non-directional Alist
        # Pick child from nDAlist and for child in dir Alist,
        # if dir of child is not to parent change direction of child to parent +1
        # if dir of child not exist, add it
        # run a bfs and keep marking nodes as visited each time we pop them
        # return count of dir changes or adds
        dirMap = defaultdict(set)
        ndirMap = defaultdict(set)
        for u,v in connections:
            dirMap[u].add(v)
            ndirMap[u].add(v)
            ndirMap[v].add(u)
        # print(dirMap,ndirMap)
        visited = set([0])
        count = 0
        queue = deque([0])
        while queue:
            # print(queue)
            parent = queue.popleft()
            for child in ndirMap[parent]:
                if child not in visited:
                    if ((child not in dirMap) or (parent not in dirMap[child])):
                        if child in dirMap[parent]:
                            dirMap[parent].remove(child)
                        dirMap[child].add(parent)
                        count += 1
                
                    visited.add(child)
                    queue.append(child)
        return count

        # {
            # 0: [],
            # 1: [3,0],
            # 2: [3],
            # 4: [0,5]
        # } 
        # queue = [1,4]
        # visited = {0,1,4}
        # {0: [1,4],
        #  1: [3,0],
        #  2: [3],
        #  3: [1,2]
        #  5: [4]
        #  4: [0,5]

        # }
        # {1: [0, 2], 
        #  3: [2, 4]}
        # queue = [2]
        # visited = {0,1,2}
        #{1: [0, 2], 
        # 0: [1],
        # 2: [1, 3], 
        # 3: [2, 4], 
        # 4: [3]}

# Faster solution from community
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in connections:
            graph[u].append((v, 1))
            graph[v].append((u, 0))

        count = 0
        
        stack = [(0, -1)]

        while stack:
            curr, prev = stack.pop()

            for neigh, sign in graph[curr]:
                if neigh != prev:
                    count += sign
                    stack.append((neigh, curr))
        
        return count