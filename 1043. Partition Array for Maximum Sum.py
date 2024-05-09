class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # Initialize an array to save the max sum until that point
        n = len(arr)
        dp = [0]*(n+1)
        
        for i in range(n):
            # In each step we calculate the max till that step
            maxVal = maxSum = 0

            for j in range(i,max(-1,i-k),-1):
                # We take the maxVal and calculate the max sum till that value
                maxVal = max(maxVal,arr[j])

                maxSum = max(maxSum, maxVal*(i-j+1) + dp[j])
            # Then we update this maxSum
            dp[i+1] = maxSum
        
        return dp[-1] # Return the last value which is the max of array