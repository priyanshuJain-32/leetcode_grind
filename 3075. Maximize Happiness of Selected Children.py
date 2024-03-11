class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        sub = 0
        ans = 0
        i = 0
        for _ in range(k):
            a = happiness[i]-sub
            if a<=0:
                break
            ans += a
            i+=1
            sub+=1
        return ans