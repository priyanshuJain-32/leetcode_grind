class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        for n,i in zip(nums, index):
            ans = ans[:i]+[n]+ans[i:]
        return ans