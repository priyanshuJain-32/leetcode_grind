class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n,total,maxL = len(nums),0,0
        pref = {0:-1}
        for i,n in enumerate(nums):
            total += n if n else -1
            try:
                maxL = max(maxL, i-pref[total])
            except:
                pref[total] = i
        return maxL