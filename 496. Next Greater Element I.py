class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = defaultdict(int)
        stack = []
        i = 0
        while i<len(nums2):
            if stack and nums2[i]>stack[-1]:
                d[stack.pop()] = nums2[i]
            else:
                d[nums2[i]] = -1
                stack.append(nums2[i])
                i += 1
        
        return [d[i] for i in nums1]