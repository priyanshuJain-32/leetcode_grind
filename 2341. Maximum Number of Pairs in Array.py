class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i]+=1
        ans = [0,0]
        for k,v in d.items():
            ans[0] += v//2
            ans[1] += v%2
        return ans