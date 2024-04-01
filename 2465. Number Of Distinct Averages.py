class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        i,j = 0, len(nums)-1
        avg = set()
        while i<j:
            avg.add((nums[i]+nums[j])/2)
            i+=1
            j-=1
        return len(avg)
