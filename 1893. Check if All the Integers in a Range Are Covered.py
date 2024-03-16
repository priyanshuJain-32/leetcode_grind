class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        all_num = set()
        seen = set(range(left,right+1))
        for l,r in ranges:
            seen = seen - set(range(l,r+1))
            if not seen:
                break
        if len(seen)!=0:
            return False
        return True