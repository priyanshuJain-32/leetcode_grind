class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n<2:
            return 0
        
        i,j=0,1
        total = 0
        
        while j<n:
            diff = prices[j]-prices[i]
            if diff<=0:
                i=j
                j+=1
            elif diff>0:
                total += diff
                i+=1
                j+=1
        return total                
