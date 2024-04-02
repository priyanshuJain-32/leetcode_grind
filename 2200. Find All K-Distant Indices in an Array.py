class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        seen = set()
        l = 0
        n = len(nums)
        for i,v in enumerate(nums):
            if v==key:
                while l<=i+k:
                    if abs(l-i)<=k and l<n:
                        seen.add(l)
                    l+=1
        return sorted(seen)
        
        # My slow approach
        # dist_idx = set()
        # for i,v in enumerate(nums):
        #     if v==key:
        #         for l in range(i-k,i+k+1):
        #             if l not in dist_idx:
        #                 dist_idx.add(l)
        # ans = []
        # for i in range(len(nums)):
        #     if i in dist_idx:
        #         ans.append(i)
        # return ans