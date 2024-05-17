class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l<r:
            m = (l+r)//2
            if nums[m]<nums[m+1]:
                l = m+1
            else:
                r = m
        return l
            



class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return 0
        left = 0
        right = n-1
        while left<=right:
            mid = (left+right)//2
            if mid==0:
                if nums[mid]>nums[mid+1]:
                    return mid
                else:
                    left = mid +1
            elif mid==n-1:
                if nums[mid]>nums[mid-1]:
                    return mid
                else:
                    right = mid-1
            else:
                if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                    return mid
                else:
                    if nums[mid]<nums[mid-1]:
                        right = mid -1
                    else:
                        left = mid+1
        return -1
