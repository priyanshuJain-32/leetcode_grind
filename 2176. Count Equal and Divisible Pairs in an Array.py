class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # Naive approach
        ans = 0
        n = len(nums)
        for i in range(0,n-1):
            for j in range(i+1, n):
                if nums[i]==nums[j] and i*j%k==0:
                    ans+=1
        return ans

        # 1000 ways of not making a bulb
        # for i in range(0,n-1):
        #     if i%k==0:
        #         for j in range(i+1, n,1):
        #             # print(j)
        #             if nums[i]==nums[j]:
        #                 # print(i,nums[i])
        #                 ans += 1
        #     else:
        #         for j in range(k*(i//k)+k,n,k):
        #             # print(j)
        #             if nums[i]==nums[j]:
        #                 # print(i,nums[i])
        #                 ans += 1
        # return ans