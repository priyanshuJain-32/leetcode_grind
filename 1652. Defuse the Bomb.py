class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        code = code*2
        ans = [0]*n
        if k==0:
            return ans
        elif k>0:
            for i in range(n):
                ans[i] = sum(code[i+1:i+1+k])
        else:
            for i in range(n-1,-1,-1):
                ans[i] = sum(code[n+i+k:n+i])
        return ans