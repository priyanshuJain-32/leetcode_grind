class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def check(num):
            s = str(num)
            for c in s:
                if c=="1":
                    continue
                if c=="0":
                    return False
                if num%int(c)!=0:
                    return False
            return True
        ans = []
        for i in range(left, right+1):
            if check(i):
                yield i
        return