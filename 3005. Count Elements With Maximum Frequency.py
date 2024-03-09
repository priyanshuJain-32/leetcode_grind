class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = defaultdict(int)
        max_freq = 0
        for i in nums:
            d[i] += 1
            max_freq = max(max_freq, d[i])
        ans = 0
        for k,v in d.items():
            if v==max_freq:
                ans += v
        return ans