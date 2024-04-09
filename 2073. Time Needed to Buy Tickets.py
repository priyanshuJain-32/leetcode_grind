class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        while tickets[k]!=0:
            i = 0
            while i<len(tickets):
                if tickets[i]==0:
                    i+=1
                    continue
                tickets[i]-=1
                ans += 1
                if i==k and tickets[k]==0:
                    break
                i+=1
        return ans