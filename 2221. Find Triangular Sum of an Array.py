class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        # Community Pascal Triangle approach
        m = len(nums)
        combination = [n*comb(m-1,i) for i,n in enumerate(nums)]
        return sum(combination)%10
        
        # My n2 approach
        n = len(nums)
        while n>1:
            temp = [0]*(n-1)
            for i in range(n-1):
                s = nums[i]+nums[i+1]
                temp[i] = s%10
            n = len(temp)
            nums = temp
        return nums[0]