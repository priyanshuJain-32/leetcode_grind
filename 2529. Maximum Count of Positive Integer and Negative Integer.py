class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def bsearch(nums, n, v=0):
            l = 0
            r = n-1
            while l<=r:
                m = (l+r)//2
                if nums[m]==0:
                    return m
                elif nums[m]>0:
                    r = m-1
                else:
                    l=m+1
            return l-1

        n = len(nums)
        idx = bsearch(nums,n,0)
        if idx==-1:
            return len(nums)
        neg = 0
        i = idx
        while i>-1:
            if nums[i]<0:
                neg = i+1
                break
            i -=1
        pos = 0
        i = idx
        while i<n:
            if nums[i]>0:
                pos = n-i
                break
            i+=1

        return max(neg, pos)