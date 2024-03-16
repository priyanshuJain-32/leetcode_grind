class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        prefix = list(accumulate(sorted(nums)))
        m = len(prefix)
        def binary(L, n, v):
            l = 0
            r = n-1
            while l<=r:
                mid = (l+r)//2
                if L[mid]==v:
                    return mid+1
                elif L[mid]>v:
                    r = mid-1
                else:
                    l = mid+1
            return r+1
        ans = []
        for i in queries:
            ans.append(binary(prefix, m, i))
        return ans