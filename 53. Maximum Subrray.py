class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_now = 0
        max_so_far = 0
        flag = False
        for i in nums:
            if i>0:
                flag = True
            max_now += i
            max_so_far = max(max_now, max_so_far)
            if max_now < 0:
                max_now = 0
        return max_so_far if flag else max(nums)
