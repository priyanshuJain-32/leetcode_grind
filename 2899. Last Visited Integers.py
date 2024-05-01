class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen = deque()
        ans = []
        k = 0
        for n in nums:
            if n>0:
                k = 0
                seen.appendleft(n)
            else:
                k+=1
            if k>0:
                try:
                    ans.append(seen[k-1])
                except: 
                    ans.append(-1)
        return ans