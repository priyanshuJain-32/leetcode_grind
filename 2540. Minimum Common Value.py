class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i,j = 0, 0
        n, m = len(nums1), len(nums2)
        while nums1[i]!=nums2[j]:
            if nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
            if i==n or j==m:
                return -1
        return nums2[j] if m>n else nums1[i]