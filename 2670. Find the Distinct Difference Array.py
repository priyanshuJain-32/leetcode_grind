class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        set1 = set()
        for i in range(n):
            set1.add(nums[i])
            set2 = set()
            for j in range(i+1, n):
                set2.add(nums[j])
            ans[i] = len(set1)-len(set2)
        return ans