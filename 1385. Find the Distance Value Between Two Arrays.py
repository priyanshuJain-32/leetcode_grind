class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        cnt = 0
        for a in arr1:
            flag = True
            for b in arr2:
                if abs(a-b) <= d:
                    flag = False
                    break
            if flag: cnt += 1
        return cnt