class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        shift_count = 0
        while left<right:
            shift_count += 1
            left >>=1
            right >>=1
        return left<<shift_count
