class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans += int(max(str(num))*len(str(num)))
        return ans