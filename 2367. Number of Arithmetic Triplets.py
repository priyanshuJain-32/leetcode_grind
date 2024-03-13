class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        cnt = 0
        for i in range(n-2):
            for j in range(i+1,n-1):
                if nums[j]-nums[i]!=diff:
                    continue
                for k in range(j+1,n):
                    if nums[k]-nums[j]==diff:
                        cnt +=1
        return cnt