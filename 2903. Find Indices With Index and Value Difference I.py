class Solution:
    def findIndices(self, nums: List[int], iD: int, vD: int) -> List[int]:
        n = len(nums)
        for i in range(n-iD):
            for j in range(i+iD,n):
                if abs(nums[i]-nums[j])>=vD:
                    return [i,j]
        return [-1,-1]