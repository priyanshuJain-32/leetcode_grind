class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l,r,max_len,max_c=0,0,0,0
        n = len(nums)
        d=defaultdict(int)
        while r<n:
            d[nums[r]]+=1
            while d[nums[r]]>k:
                d[nums[l]]-=1
                l+=1
            max_len = max(max_len, r-l+1)
            r+=1
        return max_len