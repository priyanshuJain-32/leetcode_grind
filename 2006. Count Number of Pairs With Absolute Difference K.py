class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = 0
        for i in range(n-1):
            for j in range(i+1,n):
                if abs(nums[i]-nums[j])==k:
                    cnt += 1
        return cnt

# Faster
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        d = defaultdict(int)
        for i in nums:
            d[i]+=1
        m = len(d.keys())
        keys = list(d.keys())
        cnt = 0
        keys.sort()
        for i in range(m-1):
            for j in range(i+1,m):
                if abs(keys[i]-keys[j])==k:
                    cnt+=d[keys[i]]*d[keys[j]]
        return cnt