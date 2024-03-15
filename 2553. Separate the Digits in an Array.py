class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            ans.extend(list(map(int,list(str(i)))))
        return ans