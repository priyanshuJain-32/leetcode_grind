class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainderMap = {0:-1}
        remainder = 0
        for i,n in enumerate(nums):
            remainder += n
            remainder %= k
            if remainder in remainderMap:
                if i-remainderMap[remainder]>=2:
                    return True
            else:
                remainderMap[remainder] = i
        return False

        

        # n = len(nums)
        # i = j = tot = 0
        # while i<n and j<n:
        #     if tot>6:
        #         tot-=nums[i]
        #         i += 1
        #     else:
        #         tot+=nums[j]
        #         j += 1
        #     if tot==6:
        #         return True
        # if j==n and tot>6:
        #     while tot>6:
        #         tot -= nums[i]
        #         i += 1
        # return False
            
        # # # dp = defaultdict()
        # # n = len(nums)
        # # for i in range(2,n+1):
        # #     for j in range(0,len(nums)-i+1):
        # #         temp = sum(nums[j:j+i])
        # #         if temp%k==0:
        #             return True
        #         # dp.append(temp)
        #     # print(dp)
        #     # nums = dp.copy()
        #     # dp = []

        # return False