class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for i in nums:
            if i>0:
                pos.append(i)
            else:
                neg.append(i)
        nums[0:len(nums):2] = pos
        nums[1:len(nums):2] = neg
        return nums