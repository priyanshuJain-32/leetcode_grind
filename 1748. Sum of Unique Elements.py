class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for i in nums:
            d[i]+=1
        ans = 0
        for k,v in d.items():
            if v==1:
                ans += k
        return ans