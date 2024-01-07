class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if nums==[]:
            return
        c = random.choice(nums)
        l = [i for i in nums if i>c]
        m = [i for i in nums if i==c]
        r = [i for i in nums if i<c]
        ll = len(l)
        ml = len(m)
        if ll>=k:
            return self.findKthLargest(l, k)
        elif k>ll+ml:
           return self.findKthLargest(r, k-ll-ml)
        else:
            return m[0]
