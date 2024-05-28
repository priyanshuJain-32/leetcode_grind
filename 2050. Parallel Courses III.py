class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # create a adjacency list with directed edges a:[b,c]
        aList = defaultdict(list)
        # unvisited = set(list(range(1,n+1)))

        indegree = [0]*(n+1)
        startTime = [0]*(n+1)
        # Mark indegree of nodes
        for (u,v) in relations:
            aList[u].append(v)
            indegree[v] += 1
        # Those with indegree 0 have start time of 0
        # add these nodes to startQ
        startQ = deque()
        for node in range(1,n+1):
            if indegree[node]==0:
                startQ.append(node)
        seen = maxTime = 0
        nextAvail = []
        # popleft and pick the node, reduce indegree by 1
        while seen<n:
            seen += len(startQ)
            # print(seen)
            currTime = float('inf')
            while startQ:
                curr = startQ.popleft()
                # unvisited.remove(curr)
                indegree[curr] -= 1
                # set maxtime to max of starttime[i] + time[i]
                maxTime = max(startTime[curr]+time[curr-1],maxTime)
                # for the children nodes mark start time as max of starttime so far from parents end time
                for child in aList[curr]:
                    indegree[child] -= 1
                    # keep adding nodes to nextAvail courses if indegree is 0
                    if indegree[child]==0:
                        nextAvail.append(child)
                    startTime[child] = max(startTime[child],startTime[curr]+time[curr-1])
                    currTime = min(currTime,startTime[child])
            # after finishing nodes with start times zero and emptying queue
            # increment current time by 1
            for node in nextAvail:
                # Check at the current time which nodes are starttime<currenttime and indegree==0 add them to startQ
                # repeat until we have finished all the courses
                if indegree[node]==0:
                    if startTime[node]<=currTime:
                        startQ.append(node)
                        nextAvail.remove(node)
        
        return maxTime