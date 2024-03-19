class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        max_xor = -1
        for i in nums:
            for j in nums:
                if abs(i-j)<=min(i,j):
                    xor = i^j
                    if max_xor<xor:
                        max_xor = xor
        return max_xor