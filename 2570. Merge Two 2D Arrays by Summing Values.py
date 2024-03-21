class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = collections.defaultdict(int)
        for a,b in nums1+nums2:
            d[a]+=b
        return [[k,d[k]] for k in sorted(d.keys())]