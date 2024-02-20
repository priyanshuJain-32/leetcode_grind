class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i, j, n = 0, 1, len(nums)
        while i<j and j<n:
            if nums[i]==0:
                if nums[j]!=0:
                    nums[i], nums[j] = nums[j], nums[i]
                    i+=1
                    j+=1
                else:
                    j+=1
            else:
                if j==0:
                    nums[i], nums[j] = nums[j], nums[i]
                i+=1
                j+=1