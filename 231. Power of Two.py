class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<1 or n%2==1 and n!=1:
            return False
        import math
        ans = math.log2(n)
        return int(ans)==ans