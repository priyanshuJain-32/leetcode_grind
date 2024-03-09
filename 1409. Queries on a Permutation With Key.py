class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]: 
        p = deque()
        for i in range(1,m+1):
            p.append(i)
        ans = []
        for i in queries:
            ans.append(p.index(i))
            p.remove(i)
            p.appendleft(i)
        return ans