class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [1000]*(n)
        for i in range(n):
            dp[i] = min(dp[i-1],dp[i-2],0 if i<2 else 1000000) + cost[i]
        return min(dp[-1],dp[-2])
        
        # if n==2:
        #     return min(cost[0],cost[1])
        # if n==3:
        #     return min(cost[0]+cost[2],cost[1])
        # prefix_1 = [0]*(n+1)
        # prefix_2 = [0]*(n+1)
        # prefix_1[0] = 0
        # prefix_2[0] = 0
        # prefix_2[1] = 0
        # prefix_1[1] = cost[0]
        # for i in range(2,n+1):
        #     prefix_1[i] = min(prefix_1[i-1]+cost[i-1],cost[i-2]+prefix_1[i-2])
        #     prefix_2[i] = min(prefix_2[i-1]+cost[i-1],cost[i-2]+prefix_2[i-2])
        # print(prefix_1, prefix_2)
        # return min(prefix_1[-1], prefix_2[-1])