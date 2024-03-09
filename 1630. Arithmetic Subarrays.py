class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(L, n):
            L.sort()
            d = L[0]-L[1]
            for i in range(n-1):
                if L[i]-L[i+1]!=d:
                    return False
            return True
        ans = []
        for i,j in zip(l,r):
            ans.append(check(nums[i:j+1],j-i+1))
        return ans