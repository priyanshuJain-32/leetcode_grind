class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        max_len = 0
        pref = {0:-1}
        # pref[0] = -1
        for i in range(n):
            if nums[i]:
                total += 1
            else:
                total -= 1
            try:
                max_len = max(max_len, i-pref[total])
            except:
                pref[total] = i
        return max_len