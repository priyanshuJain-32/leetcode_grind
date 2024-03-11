class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]: 
        d = defaultdict(lambda:-1)
        n = len(nums)
        temp = sorted(nums)
        for i in range(n):
            d[temp[i]] = min(i,d[temp[i]]) if d[temp[i]]!=-1 else i
        ans = [0]*n
        for j in range(n):
            ans[j] = d[nums[j]]
        return ans
        