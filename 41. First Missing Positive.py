class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Popular approach

        # Change <=0 and greater than n to n+1
        # Use digits as indices and mark as -1
        # Find pos index and return index+1
        
        
        
        # First approach
        nums = set(nums)
        for i in range(1,max(nums)+2):
            if i not in nums:
                return i
        return 1