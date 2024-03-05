class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)):
            try:
                nums.remove(val)
            except:
                return len(nums)
        return len(nums)

        # i = 0
        # count = 0
        # while i<len(nums):
        #     if nums[i]==val:
        #         nums[i]=101
        #         count +=1
        #     i+=1
        # nums.sort()
        # return i-count