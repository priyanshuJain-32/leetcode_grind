class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_count = [0]*(n+1)
        trusts_count = [0]*(n+1)

        for i,j in trust:
            trusted_count[j] += 1
            trusts_count[i] += 1
        
        for i in range(1,n+1):
            if trusted_count[i]==n-1 and trusts_count[i]==0:
                return i
                
        return -1