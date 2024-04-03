class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.arr = [0]+[nums[0]]+[0]*(n-1)
        for i in range(1,n):
            self.arr[i+1] = self.arr[i]+nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.arr[right+1]-self.arr[left]