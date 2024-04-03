class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1, d2 = collections.defaultdict(int), collections.defaultdict(int)
        for n1 in nums1:
            d1[n1]+=1
        for n2 in nums2:
            d2[n2]+=1
        ans = []
        for k,v in d1.items():
            if k in d2:
                ans.extend([k]*min(d1[k],d2[k]))
        return ans