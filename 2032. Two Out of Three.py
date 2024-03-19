class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)
        l = set()
        for i in set1.intersection(set2):
            l.add(i)
        for j in set2.intersection(set3):
            l.add(j)
        for k in set3.intersection(set1):
            l.add(k)
        return list(l)