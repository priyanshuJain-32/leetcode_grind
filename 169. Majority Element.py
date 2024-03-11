class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return statistics.mode(nums)
        # d = defaultdict(int)
        # n = len(nums)
        # for i in nums:
        #     d[i] += 1
        #     if d[i]>n//2:
        #         return i
        # for k,v in d.items():
        #     if v>n/2:
        #         return k
        # s = set(nums)
        # n = len(nums)/2
        # for i in s:
        #     c = nums.count(i)
        #     if c>n:
        #         return i