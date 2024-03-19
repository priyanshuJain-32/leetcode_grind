class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def created(L):
            d = defaultdict(int)
            for i in L:
                d[i]+=1
            return d
        d1 = created(nums1)
        d2 = created(nums2)
        ans = [0,0]
        for i in d1.keys():
            if i in d2:
                ans[0]+=d1[i]
        for j in d2.keys():
            if j in d1:
                ans[1]+=d2[j]
        return ans